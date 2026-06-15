# vllm-project/vllm#14062: [Bug]: Alibaba-NLP/gte-Qwen2-7B-instruct on AMD MI300X

| 字段 | 值 |
| --- | --- |
| Issue | [#14062](https://github.com/vllm-project/vllm/issues/14062) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Alibaba-NLP/gte-Qwen2-7B-instruct on AMD MI300X

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi all. I'm performing some tests inside the container `rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6` to test AMD gpus. When I try to serve `Alibaba-NLP/gte-Qwen2-7B-instruct` with: ``` VLLM_USE_TRITON_FLASH_ATTN=0 vllm serve Alibaba-NLP/gte-Qwen2-7B-instruct --dtype float16 --max-num-seqs 512 --gpu-memory-utilization 0.95 --hf-overrides '{"is_causal": false}' --trust-remote-code ``` server loads the model without problems but at the first inference I get: ``` INFO 02-28 18:19:14 logger.py:37] Received request embd-020a9f50db4645f1bd7ea818e65c08d7-0: prompt: 'The food was delicious and the waiter...', params: PoolingParams(additional_metadata=None), prompt_token_ids: [785, 3607, 572, 17923, 323, 279, 67169, 1112, 151643], lora_request: None, prompt_adapter_request: None. INFO 02-28 18:19:14 engine.py:270] Added request embd-020a9f50db4645f1bd7ea818e65c08d7-0. CRITICAL 02-28 18:19:15 launcher.py:99] MQLLMEngine is already dead, terminating server process INFO: 172.17.0.1:53116 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error ERROR 02-28 18:19:15 engine.py:136] AttributeError('Invalid attention type encoder_onl...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Alibaba-NLP/gte-Qwen2-7B-instruct on AMD MI300X bug;rocm ### Your current environment ### 🐛 Describe the bug Hi all. I'm performing some tests inside the container `rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: n I try to serve `Alibaba-NLP/gte-Qwen2-7B-instruct` with: ``` VLLM_USE_TRITON_FLASH_ATTN=0 vllm serve Alibaba-NLP/gte-Qwen2-7B-instruct --dtype float16 --max-num-seqs 512 --gpu-memory-utilization 0.95 --hf-overrides '{...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: quest embd-020a9f50db4645f1bd7ea818e65c08d7-0: prompt: 'The food was delicious and the waiter...', params: PoolingParams(additional_metadata=None), prompt_token_ids: [785, 3607, 572, 17923, 323, 279, 67169, 1112, 151643...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: m-seqs 512 --gpu-memory-utilization 0.95 --hf-overrides '{"is_causal": false}' --trust-remote-code ``` server loads the model without problems but at the first inference I get: ``` INFO 02-28 18:19:14 logger.py:37] Rece...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Alibaba-NLP/gte-Qwen2-7B-instruct on AMD MI300X bug;rocm ### Your current environment ### 🐛 Describe the bug Hi all. I'm performing some tests inside the container `rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
