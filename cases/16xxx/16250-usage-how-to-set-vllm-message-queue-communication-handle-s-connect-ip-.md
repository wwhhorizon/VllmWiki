# vllm-project/vllm#16250: [Usage]: how to set vLLM message queue communication handle's connect_ip to 127.0.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#16250](https://github.com/vllm-project/vllm/issues/16250) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to set vLLM message queue communication handle's connect_ip to 127.0.0.1

### Issue 正文摘录

### Your current environment vLLM Version: 0.8.2 `vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" --host 0.0.0.0 --port 6015 -tp=4 ` ![Image](https://github.com/user-attachments/assets/37db0b16-8312-4a3f-bf42-00db2a34a4f4) some of the logs: ` (VllmWorker rank=0 pid=945959) [shm_broadcast.py:259] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_5efb1fd0'), local_subscribe_addr='ipc:///tmp/a8678888-e263-49f7-ba63-5f7bcca67bd5', remote_subscribe_addr=None, remote_addr_ipv6=False)` I find that the Handle's connect_ip not exist in the logs. so I use ` netstat -naop |grep '945959'` find the port 38639 used by the pid (945959). It is not safe for me that the port (38639 ) is exposed to internet, So how to set the handle's connect_ip to 127.0.0.1 ![Image](https://github.com/user-attachments/assets/b197849d-90b8-4239-b365-e945e37c92f3)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: andle's connect_ip to 127.0.0.1 usage ### Your current environment vLLM Version: 0.8.2 `vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" --host 0.0.0.0 --port 6015 -tp=4 ` ![Image](https://github.com/user-attachmen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_5efb1fd0'), local_subscribe_addr='ipc:///tmp/a8678888-e263-49f7-ba63-5f7bcca67bd5', remote_subscribe_addr=None, remote_addr_ipv6=False)` I find...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: -49f7-ba63-5f7bcca67bd5', remote_subscribe_addr=None, remote_addr_ipv6=False)` I find that the Handle's connect_ip not exist in the logs. so I use ` netstat -naop |grep '945959'` find the port 38639 used by the pid (945...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: onment vLLM Version: 0.8.2 `vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" --host 0.0.0.0 --port 6015 -tp=4 ` ![Image](https://github.com/user-attachments/assets/37db0b16-8312-4a3f-bf42-00db2a34a4f4) some of the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to set vLLM message queue communication handle's connect_ip to 127.0.0.1 usage ### Your current environment vLLM Version: 0.8.2 `vllm serve "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B" --host 0.0.0.0 --port 6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
