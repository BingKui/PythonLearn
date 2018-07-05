# 保存需要的数据
class WebSave:
    """
    网页保存
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def save(self, host, response, thread_name):
        """
        保存指定的页面
        """
        url_name = str(host).split('//')[1]
        url_name = url_name.replace('/'. '-')
        filename = self.output_dir + '/' + url_name;
        logging.debug("%s - %s - File Saved: %s" % (time.strftime(IOS_TIME_FORMAT, time.localtime()), thread_name, filename))

        try:
            saved_file = open(filename, 'w', encoding='utf-8')
            saved_file.write(str(response))
            saved_file.close()
        except IOError as e:
            logging.debug("IOError: %s" % e)