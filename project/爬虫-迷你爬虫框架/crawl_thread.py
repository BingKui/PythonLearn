def add_url(self, ans):
    """
    如果地址不与已有的重复，则添加到todo_list
    """
    if lock.acquire():
        if ans not in self.u_table.all_url:
            self.u_table.all_url[ans] = 0
            self.u_table.add_todo_list(ans)
        else:
            logging.debug("Duplicated url : %s" % ans)
        lock.release()
    else:
        logging.debug("Lock error")

def run(self):
    """
    URL 打开，保存，分析
    """
    while True:
        # 从队列中获取一个URL
        host = self.queue.get()
        try:
            url = urllib.request.urlopen(host, data=None, timeout=self.config.crawl_timeout)
            # 分析字符编码，并以该编码读取网页
            charset = ContentMetaAttributeValue.CHARSET_RE.search(url.header['content-type'])
            charset = charset and charset.group(3) or None
            response = BeautifulSoup(url.read(), 'html.parse', form_encoding=charset)
        except urllib.error.HTTPError as e:
            logging.debug("Exception: %s" % e.code)
            continue
        except urllib.errorURLError as e:
            logging.debug("Exception: %s" % e.reason)
            continue
        except Exception as e:
            logging.debug("Exception: %s" % e)
            continue
        finally:
            # 标记队列工作已完成
            self.queue.task_done()
        
        # 保存网页
        self.web_save.save(host, response, threading.current_thread().getName())

        # 如果当期网页不是最大深度，则分析该网页，提取URLs
        if self.we_parse.cur_depth < self.config.max_depth:
            ans_list = self.web_parse.parse(host, response)
            for ans in ans_list:
                self.add_url(ans)