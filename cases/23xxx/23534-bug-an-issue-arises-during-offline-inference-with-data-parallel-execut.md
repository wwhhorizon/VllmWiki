# vllm-project/vllm#23534: [Bug]: An issue arises during offline_inference with data-parallel execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#23534](https://github.com/vllm-project/vllm/issues/23534) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: An issue arises during offline_inference with data-parallel execution.

### Issue 正文摘录

### Your current environment environment: vllm=0.8.5+cu118 torch=2.6.0+cu118 examples/offline_inference/data_parallel.py script: CUDA_VISIBLE_DEVICES=0,1,2,3 python data_parallel.py \ --model xxxx \ --dp-size 4 \ --tp-size 1 ### 🐛 Describe the bug When using the provided DP script (examples/offline_inference/data_parallel.py), the run completes successfully only if all processes finish almost simultaneously—i.e., their execution times are nearly identical, as enforced by the current script. HOWEVER, If runtimes differ and any process terminates early, the remaining processes fail synchronously. In practice, I followed the script’s pattern to distribute training data across processes; naturally, this leads to uneven execution times per process. The following error then appears: INFO 08-25 16:34:44 [core_client.py:439] Core engine process 3 ready. INFO 08-25 16:34:44 [core_client.py:439] Core engine process 2 ready. INFO 08-25 16:34:44 [core_client.py:439] Core engine process 0 ready. INFO 08-25 16:34:44 [core_client.py:439] Core engine process 1 ready. Processed prompts: 100%|███████| 4/4 [00:40<00:00, 10.13s/it, est. speed input: 731.36 toks/s, output: 145.30 toks/s] Processed pro...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rch=2.6.0+cu118 examples/offline_inference/data_parallel.py script: CUDA_VISIBLE_DEVICES=0,1,2,3 python data_parallel.py \ --model xxxx \ --dp-size 4 \ --tp-size 1 ### 🐛 Describe the bug When using the provided DP scrip...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ipt: CUDA_VISIBLE_DEVICES=0,1,2,3 python data_parallel.py \ --model xxxx \ --dp-size 4 \ --tp-size 1 ### 🐛 Describe the bug When using the provided DP script (examples/offline_inference/data_parallel.py), the run comple...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: issue arises during offline_inference with data-parallel execution. bug;stale ### Your current environment environment: vllm=0.8.5+cu118 torch=2.6.0+cu118 examples/offline_inference/data_parallel.py script: CUDA_VISIBLE...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 23) ERROR 08-25 16:35:26 [core.py:398] with set_forward_context(attn_metadata, self.vllm_config): (EngineCore_3 pid=31714) ERROR 08-25 16:35:26 [core.py:398] output = self.model_runner.execute_model(scheduler_output) (E...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
