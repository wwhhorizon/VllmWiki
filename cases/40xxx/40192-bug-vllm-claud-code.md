# vllm-project/vllm#40192: [Bug]: vllm在服务claud code时会卡死

| 字段 | 值 |
| --- | --- |
| Issue | [#40192](https://github.com/vllm-project/vllm/issues/40192) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm在服务claud code时会卡死

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 启动命令 vllm serve \ /root/hf_model/Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 \ --served-model=pkumlm_img \ --tensor-parallel-size 4 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ --enable-chunked-prefill \ --enable-prefix-caching \ --async-scheduling \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --reasoning-parser qwen3 \ --tool-call-parser qwen3_coder \ --enable-auto-tool-choice \ --mm-encoder-attn-backend TORCH_SDPA \ --enable-expert-parallel \ --max-num-batched-tokens 4096 \ --max-cudagraph-capture-size 8 \ --max-num-seqs 4 \ --gpu-memory-utilization 0.95 \ --max-model-len 262144 claude code启动命令 ANTHROPIC_BASE_URL=http://192.168.1.36:63036 \ ANTHROPIC_API_KEY=dummy \ ANTHROPIC_AUTH_TOKEN=dummy \ ANTHROPIC_DEFAULT_OPUS_MODEL=pkumlm_img \ ANTHROPIC_DEFAULT_SONNET_MODEL=pkumlm_img \ ANTHROPIC_DEFAULT_HAIKU_MODEL=pkumlm_img \ claude 运行cc，日志信息没有任何报错，观察gpu，也没有在使用，nvitop的运行如下所示 但是实际上vllm已经不响应任何请求，表现为卡死状态 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bug 启动命令 vllm serve \ /root/hf_model/Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 \ --served-model=pkumlm_img \ --tensor-parallel-size 4 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ --enable-chunked-prefill \ --enable...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: llel-size 4 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ --enable-chunked-prefill \ --enable-prefix-caching \ --async-scheduling \ --default-chat-template-kwargs '{"enable_thinking": false}' \ --reasoning-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt environment ### 🐛 Describe the bug 启动命令 vllm serve \ /root/hf_model/Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 \ --served-model=pkumlm_img \ --tensor-parallel-size 4 \ --dtype half \ --kv-cache-dtype auto \ --block-size 16 \ -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ool-choice \ --mm-encoder-attn-backend TORCH_SDPA \ --enable-expert-parallel \ --max-num-batched-tokens 4096 \ --max-cudagraph-capture-size 8 \ --max-num-seqs 4 \ --gpu-memory-utilization 0.95 \ --max-model-len 262144 c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
