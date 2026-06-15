# vllm-project/vllm#8411: [Bug]: Pixtral inference not working correctly with LLMEngine/AsyncEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#8411](https://github.com/vllm-project/vllm/issues/8411) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pixtral inference not working correctly with LLMEngine/AsyncEngine

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This code snippets does not work ```python import PIL.Image import uuid from vllm import EngineArgs, LLMEngine from vllm import SamplingParams, TextPrompt from vllm.multimodal import MultiModalDataBuiltins MODEL_ID = "mistral-community/pixtral-12b-240910" ENGINE_ARGS = EngineArgs( model=MODEL_ID, tokenizer_mode="mistral", enable_prefix_caching=True, limit_mm_per_prompt=dict(image=4), max_num_batched_tokens=16384, ) SAMPLING_PARAM = SamplingParams() engine = LLMEngine.from_engine_args(ENGINE_ARGS) prompt = "describe the image" engine_inputs = TextPrompt(prompt=prompt) image = PIL.Image.open("demo.jpg") mm_data = MultiModalDataBuiltins(image=[image]) engine_inputs["multi_modal_data"] = mm_data engine.add_request(uuid.uuid4().hex, engine_inputs, SAMPLING_PARAM) while True: out = engine.step() for request_output in request_outputs: if request_output.finished: print(request_output) if not engine.has_unfinished_requests(): break ``` This will give an output message like: ``` File "/workspace/codes/example/vllm/pixtral-12b/venv/lib/python3.10/site-packages/vllm/model_executor/models/pixtral.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: se_ ### 🐛 Describe the bug This code snippets does not work ```python import PIL.Image import uuid from vllm import EngineArgs, LLMEngine from vllm import SamplingParams, TextPrompt from vllm.multimodal import MultiModa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ctly with LLMEngine/AsyncEngine bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This code snippets does not work ```python import PIL.Image import uuid from vllm import Engine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s(image=[image]) engine_inputs["multi_modal_data"] = mm_data engine.add_request(uuid.uuid4().hex, engine_inputs, SAMPLING_PARAM) while True: out = engine.step() for request_output in request_outputs: if request_output.f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
