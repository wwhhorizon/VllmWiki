# vllm-project/vllm#24007: [Bug]: Bug in PrefixCaching for float16 dtype on RTX 8000

| 字段 | 值 |
| --- | --- |
| Issue | [#24007](https://github.com/vllm-project/vllm/issues/24007) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bug in PrefixCaching for float16 dtype on RTX 8000

### Issue 正文摘录

Results in: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ``` ### Your current environment ### 🐛 Describe the bug Reproducing script: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams MODEL_NAME = 'Qwen/Qwen2.5-7B-Instruct' # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) # Initialize the vLLM engine llm = LLM( model=MODEL_NAME, dtype='float16', seed=0, enable_prefix_caching=True ) sampling_params = SamplingParams(temperature=0.8, seed=0, top_p=0.95, top_k=20, max_tokens=32) prefix = 'Lorem ipsum dolor sit amet consectetur adipiscing elit quisque faucibus ex sapien vitae pellentesque sem placerat in id cursus mi pretium tellus duis convallis tempus leo eu aenean sed diam urna tempor pulvinar vivamus fringilla lacus nec metus bibendum egestas iaculis massa nisl malesuada lacinia integer nunc posuere ut hendrerit.' outputs = llm.generate([prefix + 'What is your name?'], sampling_params) print([x.outputs[0].text for x in outputs]) re_output = llm.generate([prefix + 'What is your name and why?'], sampling_params) print([x.outputs[0].text for x in re_output]) ``` Code...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ching for float16 dtype on RTX 8000 bug Results in: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ``` ### Your current environment ### 🐛 Describe the bug Reproducing sc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Bug in PrefixCaching for float16 dtype on RTX 8000 bug Results in: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ``` ### Your current environment ### 🐛 Describe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Bug in PrefixCaching for float16 dtype on RTX 8000 bug Results in: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ``` ### Your current environment ### 🐛 Describe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: transformers import AutoTokenizer from vllm import LLM, SamplingParams MODEL_NAME = 'Qwen/Qwen2.5-7B-Instruct' # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) # Initialize the vLLM engin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Results in:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
