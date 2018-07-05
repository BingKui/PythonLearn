# 向队列中填充 URLs
cur_depth = 0
depth = conf.max_depth
while cur_depth <= depth:
    for host in hosts:
        url_queus.put(host)
        time.sleep(conf.crawl_interval)
    cur_depth += 1
    web_parse.cur_depth = cur_depth
    url_queue.join()
    hosts = copy.deepcopy(u_table.todo_list)
    u_table.todo_list = []