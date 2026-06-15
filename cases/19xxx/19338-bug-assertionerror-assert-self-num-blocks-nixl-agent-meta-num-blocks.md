# vllm-project/vllm#19338: [Bug]: AssertionError assert self.num_blocks >= nixl_agent_meta.num_blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#19338](https://github.com/vllm-project/vllm/issues/19338) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError assert self.num_blocks >= nixl_agent_meta.num_blocks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug node 1: ``` VLLM_NIXL_SIDE_CHANNEL_HOST=XX.XX.XX.XX \ VLLM_NIXL_SIDE_CHANNEL_PORT=18888 \ vllm serve /data/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ -tp 8 --port 8001 \ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_producer"}' ``` node2 ``` VLLM_NIXL_SIDE_CHANNEL_HOST=YY.YY.YY.YY \ VLLM_NIXL_SIDE_CHANNEL_PORT=18888 \ vllm serve /data/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ -tp 8 --port 8002 \ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_consumer"}' ``` node1 ``` python toy_proxy_sever.py --prefiller-port 8001 --decoder-port 8002 --prefiller-host XX.XX.XX.XX --decoder-host YY.YY.YY.YY vllm bench serve --model /data/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --num-prompts 1 ``` ``` python (VllmWorker rank=3 pid=2147132) ERROR 06-09 02:34:50 [multiproc_executor.py:523] WorkerProc hit an exception. (VllmWorker rank=3 pid=2147132) ERROR 06-09 02:34:50 [multiproc_executor.py:523] Traceback (most recent call last): (VllmWorker rank=3 pid=2147132) ERROR 06-09 02:34:50 [multiproc_executor.py:523] File "/data/kebe/vllm/vllm/v1/executor/multiproc_executor.py", line 518, in worker_busy_loop...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: AssertionError assert self.num_blocks >= nixl_agent_meta.num_blocks bug ### Your current environment ### 🐛 Describe the bug node 1: ``` VLLM_NIXL_SIDE_CHANNEL_HOST=XX.XX.XX.XX \ VLLM_NIXL_SIDE_CHANNEL_PORT=18888...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: DE_CHANNEL_PORT=18888 \ vllm serve /data/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \ -tp 8 --port 8001 \ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_producer"}' ``` node2 ``` VLLM_NIXL_SIDE_CHAN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: or","kv_role":"kv_consumer"}' ``` node1 ``` python toy_proxy_sever.py --prefiller-port 8001 --decoder-port 8002 --prefiller-host XX.XX.XX.XX --decoder-host YY.YY.YY.YY vllm bench serve --model /data/deepseek-ai/DeepSeek...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
