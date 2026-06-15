# vllm-project/vllm#14108: [Bug]: 使用vllm部署qwen2.5-vl系列的模型，出现调用卡死的问题，怎么解决？刚刚部署调用正常，显卡占用50%，后来使用一段时间之后，调用一次请求时间会很长，显卡占用到了90%。日志报错如下，怎么解决？

| 字段 | 值 |
| --- | --- |
| Issue | [#14108](https://github.com/vllm-project/vllm/issues/14108) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用vllm部署qwen2.5-vl系列的模型，出现调用卡死的问题，怎么解决？刚刚部署调用正常，显卡占用50%，后来使用一段时间之后，调用一次请求时间会很长，显卡占用到了90%。日志报错如下，怎么解决？

### Issue 正文摘录

### Your current environment 部署命令： CUDA_VISIBLE_DEVICES=2 vllm serve /home/li_mingze/models/Qwen/Qwen2___5-VL-7B-Instruct --tensor-parallel-size 1 --gpu-memory-utilization 0.8 --port 2003 --limit-mm-per-prompt image=5 > qwen2.5_vl_7B_instruct_2003.log 2>&1 & 日志报错： ERROR 03-03 02:48:16 client.py:300] RuntimeError('Engine process (pid 2218951) died.') ERROR 03-03 02:48:16 client.py:300] NoneType: None CRITICAL 03-03 02:48:17 launcher.py:101] MQLLMEngine is already dead, terminating server process INFO: 10.8.21.37:38638 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error INFO: Shutting down INFO: Waiting for application shutdown. INFO: Application shutdown complete. INFO: Finished server process [2218746] /data23/ljc/anaconda3/envs/imdv2/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ### 🐛 Describe the bug 部署命令： CUDA_VISIBLE_DEVICES=2 vllm serve /home/li_mingze/models/Qwen/Qwen2___5-VL-7B-Instruct --tensor-parallel-size 1 --gpu-memory-utilization 0.8 --port 2003 --limit-mm-per-prompt image=5 > qwen2.5_vl_7B...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 会很长，显卡占用到了90%。日志报错如下，怎么解决？ bug;stale ### Your current environment 部署命令： CUDA_VISIBLE_DEVICES=2 vllm serve /home/li_mingze/models/Qwen/Qwen2___5-VL-7B-Instruct --tensor-parallel-size 1 --gpu-memory-utilization 0.8 --port...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 使用vllm部署qwen2.5-vl系列的模型，出现调用卡死的问题，怎么解决？刚刚部署调用正常，显卡占用50%，后来使用一段时间之后，调用一次请求时间会很长，显卡占用到了90%。日志报错如下，怎么解决？ bug;stale ### Your current environment 部署命令： CUDA_VISIBLE_DEVICES=2 vllm serve /home/li_mingze/models/Qwen/Qwe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ，怎么解决？刚刚部署调用正常，显卡占用50%，后来使用一段时间之后，调用一次请求时间会很长，显卡占用到了90%。日志报错如下，怎么解决？ bug;stale ### Your current environment 部署命令： CUDA_VISIBLE_DEVICES=2 vllm serve /home/li_mingze/models/Qwen/Qwen2___5-VL-7B-Instruct --tensor-parallel-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
