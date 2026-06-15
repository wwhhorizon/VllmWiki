# vllm-project/vllm#8990: [Bug]: MiniCPMV Raises UnboundLocalError When Image Placeholder is Omitted

| 字段 | 值 |
| --- | --- |
| Issue | [#8990](https://github.com/vllm-project/vllm/issues/8990) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniCPMV Raises UnboundLocalError When Image Placeholder is Omitted

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There's a small bug in `MiniCPM-V` if a prompt is provided, but the user mistakenly omits the image placeholder. Example: ```python from vllm import LLM, SamplingParams from PIL import Image model_name = "openbmb/MiniCPM-V-2_6" llm = LLM( model=model_name, trust_remote_code=True, ) sampling_params = SamplingParams() img = Image.open("cherry_blossom.jpg") outputs = llm.generate( { "prompt": "I have no image tag", "multi_modal_data": {"image": img} }, sampling_params=sampling_params ) ``` raises `UnboundLocalError: local variable 'token_ids' referenced before assignment`, because the variable is only defined if the prompt is `None` ([here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/minicpmv.py#L278)), but it's used if there are no image tags [here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/minicpmv.py#L288). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er mistakenly omits the image placeholder. Example: ```python from vllm import LLM, SamplingParams from PIL import Image model_name = "openbmb/MiniCPM-V-2_6" llm = LLM( model=model_name, trust_remote_code=True, ) sampli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Model Input Dumps _No response_ ### 🐛 Describe the bug There's a small bug in `MiniCPM-V` if a prompt is provided, but the user mistakenly omits the image placeholder. Example: ```python from vllm import LLM, Sampli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: en Image Placeholder is Omitted bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There's a small bug in `MiniCPM-V` if a prompt is provided, but the user mistakenly omits the i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
