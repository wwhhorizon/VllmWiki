# vllm-project/vllm#41456: [Bug]: “max_model_len” in “--speculative-config” is invalid

| 字段 | 值 |
| --- | --- |
| Issue | [#41456](https://github.com/vllm-project/vllm/issues/41456) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: “max_model_len” in “--speculative-config” is invalid

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /models/Qwen3.6-27B-FP8 \ --port 23334 --host 0.0.0.0 \ --api-key sk-123456 \ --tensor-parallel-size 4 \ --max-model-len 200000 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --limit-mm-per-prompt '{"video": 0}' \ --served-model-name llm21 \ --gpu-memory-utilization 0.82 \ --dtype half \ --kv-cache-dtype auto \ --enable-chunked-prefill \ --model-impl vllm \ --speculative-config '{"method":"mtp","num_speculative_tokens":3,"max_model_len":200000}' \ --performance-mode interactivity \ --enable-prefix-caching \ --disable-custom-all-reduce \ --attention-config.backend FLASHINFER \ --max_num_seqs 5 mtp models load max_model_len is 256K not 200000 (APIServer pid=451139) INFO 05-01 19:38:30 [model.py:549] Resolved architecture: Qwen3_5ForConditionalGeneration (APIServer pid=451139) WARNING 05-01 19:38:30 [model.py:2016] Casting torch.bfloat16 to torch.float16. (APIServer pid=451139) INFO 05-01 19:38:30 [model.py:1678] Using max model len 200000 (APIServer pid=451139) INFO 05-01 19:38:30 [model.py:549] Resolved architecture: Qwen3_5MTP (APIServer pid=451139) WARNING 05-01 19:38:30...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: vironment ### 🐛 Describe the bug ``` vllm serve /models/Qwen3.6-27B-FP8 \ --port 23334 --host 0.0.0.0 \ --api-key sk-123456 \ --tensor-parallel-size 4 \ --max-model-len 200000 \ --reasoning-parser qwen3 \ --enable-auto-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: le-prefix-caching \ --disable-custom-all-reduce \ --attention-config.backend FLASHINFER \ --max_num_seqs 5 mtp models load max_model_len is 256K not 200000 (APIServer pid=451139) INFO 05-01 19:38:30 [model.py:549] Resol...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: “max_model_len” in “--speculative-config” is invalid bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve /models/Qwen3.6-27B-FP8 \ --port 23334 --host 0.0.0.0 \ --api-key sk-123456 \ --tensor-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0000 (APIServer pid=451139) INFO 05-01 19:38:30 [model.py:549] Resolved architecture: Qwen3_5ForConditionalGeneration (APIServer pid=451139) WARNING 05-01 19:38:30 [model.py:2016] Casting torch.bfloat16 to torch.float16...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
