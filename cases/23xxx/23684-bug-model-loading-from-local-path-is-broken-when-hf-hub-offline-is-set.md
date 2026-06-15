# vllm-project/vllm#23684: [Bug]: Model loading from local path is broken when HF_HUB_OFFLINE is set to 1

| 字段 | 值 |
| --- | --- |
| Issue | [#23684](https://github.com/vllm-project/vllm/issues/23684) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model loading from local path is broken when HF_HUB_OFFLINE is set to 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For offline inference, model loading from local path is broken when HF_HUB_OFFLINE is set to 1. I am trying to load a model form local path for offline inferencing using code similar to below. `/local/path/to/model` is the path to a model that contains HuggingFace model snapshot. ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/local/path/to/model") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` When I try to run this code after setting `HF_HUB_OFFLINE=1`, `LocalEntryNotFoundError` exception is raised with this error message: ```"Cannot find an appropriate cached snapshot folder for the specified revision on the local disk and outgoing traffic has been disabled. To enable repo look-ups and downloads online, pass 'local_files_only=False' as input."``` This work...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Model loading from local path is broken when HF_HUB_OFFLINE is set to 1 bug ### Your current environment ### 🐛 Describe the bug For offline inference, model loading from local path is broken when HF_HUB_OFFLINE i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: et to 1. I am trying to load a model form local path for offline inferencing using code similar to below. `/local/path/to/model` is the path to a model that contains HuggingFace model snapshot. ``` from vllm import LLM,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rontend_api;hardware_porting;model_support;sampling_logits cuda;sampling;triton build_error env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: . To enable repo look-ups and downloads online, pass 'local_files_only=False' as input."``` This workflow used to work without any issues until recently before this PR was merged: https://github.com/vllm-project/vllm/pu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23694: Should have ROCm label: NO (0 matches) #23684: Should have ROCm label: NO (0 matches) #23681: Should have ROCm label: NO (0 matches) #23674: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
