# vllm-project/vllm#16254: [Bug]: Problem Load llama3.2-11B-Vision-Instruct-INT4-GPTQ

| 字段 | 值 |
| --- | --- |
| Issue | [#16254](https://github.com/vllm-project/vllm/issues/16254) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Problem Load llama3.2-11B-Vision-Instruct-INT4-GPTQ

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a model named llama3.2-11B-Vision-Instruct-INT4-GPTQ. From the name, it's mllama structured model which is quantized using GPTQ in 4bit. I load the model like this ``` vllm serve fahadh4ilyas/llama3.2-11B-Vision-Instruct-INT4-GPTQ --host 0.0.0.0 --served-model-name llama3.2-11B llama3.2-11B-Int4 --port 8000 --max-model-len 16384 --limit-mm-per-prompt image=3 --max-num-seqs 2 --enforce-eager ``` I got three different error from each of these commits. Here is the latest working commit for the command above 5d802522a783ba31a150df80499a71acabd8009c. Here is the first commit that I got error when running the command above 69ff99fdcddf4d6dbcebf5f750b121dd171b86a3 The second error I got is from this commit fb16eea48b4e0ac74502d1b55fb7307af2135a69 And the latest and current error I got is from this commit e392d858311a345104ce727e7301476664b3ae53 CC: @NickLucche @Isotr0py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Problem Load llama3.2-11B-Vision-Instruct-INT4-GPTQ bug ### Your current environment ### 🐛 Describe the bug I have a model named llama3.2-11B-Vision-Instruct-INT4-GPTQ. From the name, it's mllama structured model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Problem Load llama3.2-11B-Vision-Instruct-INT4-GPTQ bug ### Your current environment ### 🐛 Describe the bug I have a model named llama3.2-11B-Vision-Instruct-INT4-GPTQ. From the name, it's mllama structured model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rdware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;gemm;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_depende...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
