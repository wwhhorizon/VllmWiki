# vllm-project/vllm#2345: memory leak in v0.2.7

| 字段 | 值 |
| --- | --- |
| Issue | [#2345](https://github.com/vllm-project/vllm/issues/2345) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> memory leak in v0.2.7

### Issue 正文摘录

it seem exist memory leak in v0.2.7 USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND root 1071 0.4 0.0 28963612 417336 ? SNl 17:36 0:02 ray::RayWorkerVllm root 1166 6.2 0.5 68235476 5179612 ? RNl 17:36 0:36 ray::RayWorkerVllm.execute_method two hours later USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND root 1071 0.1 0.0 28963612 417336 ? SNl 17:36 0:14 ray::RayWorkerVllm root 1166 3.4 0.6 69346516 6284616 ? SNl 17:36 4:57 ray::RayWorkerVllm three hours later USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND root 1071 0.1 0.0 28963612 417336 ? SNl 17:36 0:20 ray::RayWorkerVllm root 1166 3.4 0.6 69987220 6919976 ? SNl 17:36 7:27 ray::RayWorkerVllm

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
