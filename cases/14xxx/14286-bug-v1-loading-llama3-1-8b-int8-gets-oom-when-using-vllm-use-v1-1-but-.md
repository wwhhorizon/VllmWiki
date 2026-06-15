# vllm-project/vllm#14286: [Bug][V1]: Loading Llama3.1-8B-INT8 gets OOM when using VLLM_USE_v1=1 but safe using v0

| 字段 | 值 |
| --- | --- |
| Issue | [#14286](https://github.com/vllm-project/vllm/issues/14286) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: Loading Llama3.1-8B-INT8 gets OOM when using VLLM_USE_v1=1 but safe using v0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a Llama3.1 model with this config I load it using vllm like this ```bash VLLM_USE_V1=1 vllm serve models/llama3.1-8B-INT8 --host 0.0.0.0 --served-model-name llama3.1-8B llama3.1-8B-Int8 --port 8000 --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser llama3_json ``` But, I got this error If I load it using vllm like this ```bash vllm serve models/llama3.1-8B-INT8 --host 0.0.0.0 --served-model-name llama3.1-8B llama3.1-8B-Int8 --port 8000 --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser llama3_json ``` it works perfectly fine What I know is the culprit is this commit da31b5333ec198343a79cd8b5b198ac76896de51. Because if I tried it using the commit before it which is bb78fb318e69f2e5e42ad2f6cf7dd050330c8643, it works perfectly Any explanation why this happened? cc: @JenZhao and @ywang96 EDIT: I didn't realize that the error from da31b5333ec198343a79cd8b5b198ac76896de51 is different with the error that I got from the last commit in main. After checking it more, I found that between commit da31b5333ec198343a79cd8b5b198ac76896de51 and 7f6bae561c210da06af5d40e8861b0d2ddfe339c, the error is about `S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][V1]: Loading Llama3.1-8B-INT8 gets OOM when using VLLM_USE_v1=1 but safe using v0 bug;stale ### Your current environment ### 🐛 Describe the bug I have a Llama3.1 model with this config I load it using vllm like th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Llama3.1-8B-INT8 gets OOM when using VLLM_USE_v1=1 but safe using v0 bug;stale ### Your current environment ### 🐛 Describe the bug I have a Llama3.1 model with this config I load it using vllm like this ```bash VLLM_USE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding activation;attention;cache;cuda;operator;quantization;sampling;triton build_err...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 37 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
