# vllm-project/vllm#14324: [Bug]: 'DeepseekV2Model' object has no attribute 'config' when enabling P/D Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#14324](https://github.com/vllm-project/vllm/issues/14324) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'DeepseekV2Model' object has no attribute 'config' when enabling P/D Disaggregation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I was trying Disaggregated Prefilling with DeepSeek-V2-Lite, I firstly started two backend with a proxy: ```bash CUDA_VISIBLE_DEVICES=0 python3 \ -m vllm.entrypoints.openai.api_server \ --model /workspace/deepseek/zer/DeepSeek-V2-Lite/ \ --port 8100 \ --max-model-len 10000 \ --gpu-memory-utilization 0.95 \ --trust_remote_code \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_buffer_size":5e9}' & CUDA_VISIBLE_DEVICES=1 python3 \ -m vllm.entrypoints.openai.api_server \ --model /workspace/deepseek/zer/DeepSeek-V2-Lite/ \ --port 8200 \ --max-model-len 10000 \ --gpu-memory-utilization 0.95 \ --trust_remote_code \ --kv-transfer-config \ '{"kv_connector":"PyNcclConnector","kv_role":"kv_consumer","kv_rank":1,"kv_parallel_size":2,"kv_buffer_size":5e9}' & wait_for_server 8100 wait_for_server 8200 python3 disagg_prefill_proxy_server.py & # Listening on port 8000 ``` Then I run a benchmark test: ```bash python3 ../benchmark_serving.py \ --backend vllm \ --model /workspace/deepseek/zer/DeepSeek-V2-Lite/ \ --dataset-name "sonnet" \ --dataset-path "../sonnet_4x.txt" \ -...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: l' object has no attribute 'config' when enabling P/D Disaggregation bug;stale ### Your current environment ### 🐛 Describe the bug When I was trying Disaggregated Prefilling with DeepSeek-V2-Lite, I firstly started two...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: max_tokens=1, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: [100000, 100000, 5726,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: th DeepSeek-V2-Lite, I firstly started two backend with a proxy: ```bash CUDA_VISIBLE_DEVICES=0 python3 \ -m vllm.entrypoints.openai.api_server \ --model /workspace/deepseek/zer/DeepSeek-V2-Lite/ \ --port 8100 \ --max-m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ng Disaggregated Prefilling with DeepSeek-V2-Lite, I firstly started two backend with a proxy: ```bash CUDA_VISIBLE_DEVICES=0 python3 \ -m vllm.entrypoints.openai.api_server \ --model /workspace/deepseek/zer/DeepSeek-V2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 'DeepseekV2Model' object has no attribute 'config' when enabling P/D Disaggregation bug;stale ### Your current environment ### 🐛 Describe the bug When I was trying Disaggregated Prefilling with DeepSeek-V2-Lite,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
