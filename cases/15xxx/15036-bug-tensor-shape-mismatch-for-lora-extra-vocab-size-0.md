# vllm-project/vllm#15036: [Bug]: tensor shape mismatch for `--lora-extra-vocab-size 0`

| 字段 | 值 |
| --- | --- |
| Issue | [#15036](https://github.com/vllm-project/vllm/issues/15036) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensor shape mismatch for `--lora-extra-vocab-size 0`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When the model server is launched with `--lora-extra-vocab-size 0`(to optimize for LoRA adapter which has not been trained with extra special tokens), the engine falls short on profile run stage: If `--lora-extra-vocab-size` has not been set or set to nonzero (and no other arguments changed), the model server runs okay. ## Minimal working example ```bash VLLM_USE_V1=0 vllm serve /app/model/Llama-3.3-70B-Instruct/ --served-model-name meta-llama/Llama-3.3-70B-Instruct --gpu-memory-utilization 0.96 --tensor-parallel-size 4 --max-model-len 131072 --enable-chunked-prefill --max-num-batched-tokens 8192 --enable-auto-tool-choice --tool-call-parser llama3_json --enable-lora --fully-sharded-lora --max-loras 1 --max-lora-rank 8 --lora-extra-vocab-size 0 ``` (It doesn't even have to load pretrained LoRA adapter, the script fails anyway) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0`(to optimize for LoRA adapter which has not been trained with extra special tokens), the engine falls short on profile run stage: If `--lora-extra-vocab-size` has not been set or set to nonzero (and no other arguments...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: tensor shape mismatch for `--lora-extra-vocab-size 0` bug ### Your current environment ### 🐛 Describe the bug When the model server is launched with `--lora-extra-vocab-size 0`(to optimize for LoRA adapter which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: on 0.96 --tensor-parallel-size 4 --max-model-len 131072 --enable-chunked-prefill --max-num-batched-tokens 8192 --enable-auto-tool-choice --tool-call-parser llama3_json --enable-lora --fully-sharded-lora --max-loras 1 --...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding attention;cuda;operator;quantization;triton build_error;crash;mismatch dtype;env_dependency;sha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0` bug ### Your current environment ### 🐛 Describe the bug When the model server is launched with `--lora-extra-vocab-size 0`(to optimize for LoRA adapter which has not been trained with extra special tokens), the engin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
