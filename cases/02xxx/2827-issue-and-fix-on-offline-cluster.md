# vllm-project/vllm#2827: Issue and fix on offline cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#2827](https://github.com/vllm-project/vllm/issues/2827) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue and fix on offline cluster

### Issue 正文摘录

Hi! So was trying to run vllm on a large public cluster. The GPU can only be executed in an offline environment. While the model is pre-loaded, vllm is still trying to find an IP, I guess in case there will be some download at some point. So ending up with errors like: > get_ip(), get_open_port()) > ^^^^^^^^ > File "/linkhome/rech/genrug01/uft12cr/.local/lib/python3.11/site-packages/vllm/utils.py", line 166, in get_ip > s.connect(("8.8.8.8", 80)) # Doesn't need to be reachable > ^^^^^^^^^^^^^^^^^^^^^^^^^^ > OSError: [Errno 101] Network is unreachable Has been fixed thanks to the feedback from cluster engineers by rewriting get_ip in utils.py with: ```python def get_ip() -> str: try: s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) s.connect(("8.8.8.8", 80)) # Doesn't need to be reachable ip_sock = s.getsockname()[0] except: import idr_torch ip_sock = idr_torch.master_addr return ip_sock ``` Quick fix, but maybe there should be some kind of fall back on idr_torch.master_addr if the ip is not too be found.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g up with errors like: > get_ip(), get_open_port()) > ^^^^^^^^ > File "/linkhome/rech/genrug01/uft12cr/.local/lib/python3.11/site-packages/vllm/utils.py", line 166, in get_ip > s.connect(("8.8.8.8", 80)) # Doesn't need...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ter. The GPU can only be executed in an offline environment. While the model is pre-loaded, vllm is still trying to find an IP, I guess in case there will be some download at some point. So ending up with errors like: >...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
