# vllm-project/vllm#1824: Local models cannot be used when the network is not accessible.

| 字段 | 值 |
| --- | --- |
| Issue | [#1824](https://github.com/vllm-project/vllm/issues/1824) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Local models cannot be used when the network is not accessible.

### Issue 正文摘录

2023-11-29 11:34:19 Traceback (most recent call last): 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py", line 467, in _make_request 2023-11-29 11:34:19 self._validate_conn(conn) 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py", line 1096, in _validate_conn 2023-11-29 11:34:19 conn.connect() 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connection.py", line 642, in connect 2023-11-29 11:34:19 sock_and_verified = _ssl_wrap_socket_and_match_hostname( 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connection.py", line 782, in _ssl_wrap_socket_and_match_hostname 2023-11-29 11:34:19 ssl_sock = ssl_wrap_socket( 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/util/ssl_.py", line 470, in ssl_wrap_socket 2023-11-29 11:34:19 ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname) 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/util/ssl_.py", line 514, in _ssl_wrap_socket_impl 2023-11-29 11:34:19 return ssl_context.wrap_socket(sock, server_hostname=server_hostname) 2023-11-29 11:3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Local models cannot be used when the network is not accessible. 2023-11-29 11:34:19 Traceback (most recent call last): 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py", line 4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: server.py:638] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='TheBloke/Yi-34B-Chat-AWQ', tokenizer=None...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, block_size=16, seed=0, swap_space=4, gpu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /python3.10/dist-packages/urllib3/connectionpool.py", line 467, in _make_request 2023-11-29 11:34:19 self._validate_conn(conn) 2023-11-29 11:34:19 File "/usr/local/lib/python3.10/dist-packages/urllib3/connectionpool.py"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
