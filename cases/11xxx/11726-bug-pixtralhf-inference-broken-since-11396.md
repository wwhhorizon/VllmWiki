# vllm-project/vllm#11726: [Bug]: PixtralHF inference broken since #11396

| 字段 | 值 |
| --- | --- |
| Issue | [#11726](https://github.com/vllm-project/vllm/issues/11726) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PixtralHF inference broken since #11396

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug PixtralHF models fail when given non `[1024x1024]` images or when given multiple images due to a regression introduced in https://github.com/vllm-project/vllm/pull/11396. I validated these errors exist for that commit on main (`101418096ffe3c83b6d541e1303b10e9d5e03861`) and don't exist for the commit before (`5ce4627a7ec4cf4e19ff4be7f030883ef486393f`). Pixel values shape error with single image: ```python from vllm import LLM, SamplingParams from vllm.assets.image import ImageAsset sampling_params = SamplingParams(temperature=0.0, max_tokens=10) model_name = "nm-testing/pixtral-12b-FP8-dynamic" llm = LLM( model=model_name, max_num_seqs=1, enforce_eager=True, max_model_len=10000, ) image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg" messages = [ { "role": "user", "content": [ {"type": "text", "text": "Describe the image."}, {"type": "image_url", "image_url": {"url": image_url}}, ], }, ] outputs = llm.chat(messages, sampling_params=sampling_params) for output in outputs: print(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 393f`). Pixel values shape error with single image: ```python from vllm import LLM, SamplingParams from vllm.assets.image import ImageAsset sampling_params = SamplingParams(temperature=0.0, max_tokens=10) model_name = "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: PixtralHF inference broken since #11396 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug PixtralHF models fail when given non `[1024x1024]` images or when given multiple...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ms(temperature=0.0, max_tokens=10) model_name = "nm-testing/pixtral-12b-FP8-dynamic" llm = LLM( model=model_name, max_num_seqs=1, enforce_eager=True, max_model_len=10000, ) image_url = "https://upload.wikimedia.org/wiki...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: en given non `[1024x1024]` images or when given multiple images due to a regression introduced in https://github.com/vllm-project/vllm/pull/11396. I validated these errors exist for that commit on main (`101418096ffe3c8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
