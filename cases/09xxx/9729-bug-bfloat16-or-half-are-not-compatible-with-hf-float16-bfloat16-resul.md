# vllm-project/vllm#9729: [Bug]: Bfloat16 or Half are not compatible with HF float16/bfloat16 result.

| 字段 | 值 |
| --- | --- |
| Issue | [#9729](https://github.com/vllm-project/vllm/issues/9729) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bfloat16 or Half are not compatible with HF float16/bfloat16 result.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've discovered that while vLLM and Hugging Face's implementation produce identical results in float32 precision, they generate different outputs when using bfloat16. This inconsistency appears to be specifically related to the precision mode rather than the general implementation. I was tested on the "PyTest Code" on `tests/models/decoder_only/language/test_models.py` with follow models: 1. "gpt2", 2. "bigcode/tiny_starcoder_py", 3. "EleutherAI/pythia-70m", 4. "bigscience/bloom-560m", 5. "microsoft/phi-2", 6. "stabilityai/stablelm-3b-4e1t", 7. "bigcode/starcoder2-3b", 8. "Qwen/Qwen2.5-1.5B", ```python """Compare the outputs of HF and vLLM when using greedy sampling. This test only tests small models. Big models such as 7B should be tested from test_big_models.py because it could use a larger instance to run tests. Run `pytest tests/models/test_models.py`. """ import pytest from ...utils import check_outputs_equal MODELS = [ # "facebook/opt-125m", "gpt2", "bigcode/tiny_starcoder_py", "EleutherAI/pythia-70m", "bigscience/bloom-560m", # Testing alibi slopes. "microsoft/phi-2", "stabilityai/stable...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nd Hugging Face's implementation produce identical results in float32 precision, they generate different outputs when using bfloat16. This inconsistency appears to be specifically related to the precision mode rather th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Bfloat16 or Half are not compatible with HF float16/bfloat16 result. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've discovered that while vLLM and Hugging Fa
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Bfloat16 or Half are not compatible with HF float16/bfloat16 result. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've discovered that while vLLM and Hugging F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: outputs of HF and vLLM when using greedy sampling. This test only tests small models. Big models such as 7B should be tested from test_big_models.py because it could use a larger instance to run tests. Run `pytest tests...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bfloat16 or Half are not compatible with HF float16/bfloat16 result. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I've discovered that while vLLM and Hugging Face's i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
