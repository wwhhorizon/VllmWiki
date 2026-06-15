# vllm-project/vllm#8450: [Bug]: when curl /chat/completions, TypeError: Unable to evaluate type annotation 'Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]'.

| 字段 | 值 |
| --- | --- |
| Issue | [#8450](https://github.com/vllm-project/vllm/issues/8450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when curl /chat/completions, TypeError: Unable to evaluate type annotation 'Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]'.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I installed vllm according to the documentation with python 3.8 and cuda 11.8 ``` # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.6.1 export PYTHON_VERSION=38 pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118 ``` Then I accessed the completions interface and everything was normal, but chat/completions reported an error ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "/models/Qwen1.5-32B-Chat-GPTQ-Int4", "prompt": "你是谁", "max_tokens": 512, "temperature": 0 }' ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I installed vllm according to the documentation with python 3.8 and cuda 11.8 ``` # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.6.1 export PYTHON_VE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cation/json" \ -d '{ "model": "/models/Qwen1.5-32B-Chat-GPTQ-Int4", "prompt": "你是谁", "max_tokens": 512, "temperature": 0 }' ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug I installed vllm according to the documentation with python 3.8 and cuda 11.8 ``` # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.6.1 export PYTHON_VERSION=38 pip install https://github.com/vllm-project/vllm/re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: letionContentPartTextParam]]]'. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I installed vllm according to the documentation with python 3.8 and cuda 11.8 ``` # Install vLL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: when curl /chat/completions, TypeError: Unable to evaluate type annotation 'Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]'. bug ### Your current environment ### Model Input Dumps _No response...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
