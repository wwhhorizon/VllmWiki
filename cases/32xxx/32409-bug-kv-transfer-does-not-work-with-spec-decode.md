# vllm-project/vllm#32409: [Bug]: KV Transfer does not work with Spec Decode

| 字段 | 值 |
| --- | --- |
| Issue | [#32409](https://github.com/vllm-project/vllm/issues/32409) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Transfer does not work with Spec Decode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello vLLM maintainers, thanks for the project! It looks like speculative decoding is incompatible with kv_transfer in my setup. When kv_transfer is enabled, speculative decoding fails consistently. I’m seeing the same behavior with gpt-oss-20b as well. **Expectation** I expected the draft/speculative model KV cache to be transferred/propagated similarly to the main model path when kv_transfer is enabled. I use v0.14.0rc1, installed by following https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#build-wheel-from-source **Reproducer** ```python from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig ktc = KVTransferConfig( kv_connector="ExampleConnector", kv_role="kv_producer", kv_connector_extra_config={"shared_storage_path": "./output3"}, ) llm = LLM( model="meta-llama/Llama-3.1-8B-Instruct", enforce_eager=True, kv_transfer_config=ktc, speculative_config={ "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 1, "method": "eagle3", }, block_size=16 ) params = SamplingParams(max_tokens=10, temperature=0.0) outputs = llm.generate(["You are an expert assistant with strong reas...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: y to the main model path when kv_transfer is enabled. I use v0.14.0rc1, installed by following https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#build-wheel-from-source **Reproducer** ```python from vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: KV Transfer does not work with Spec Decode bug ### Your current environment ### 🐛 Describe the bug Hello vLLM maintainers, thanks for the project! It looks like speculative decoding is incompatible with kv_transf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: "num_speculative_tokens": 1, "method": "eagle3", }, block_size=16 ) params = SamplingParams(max_tokens=10, temperature=0.0) outputs = llm.generate(["You are an expert assistant with strong reasoning, writing, and planni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: eculative decoding fails consistently. I’m seeing the same behavior with gpt-oss-20b as well. **Expectation** I expected the draft/speculative model KV cache to be transferred/propagated similarly to the main model path...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
