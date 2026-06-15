# vllm-project/vllm#12183: [Bug]: Fail to use beamsearch with llm.chat

| 字段 | 值 |
| --- | --- |
| Issue | [#12183](https://github.com/vllm-project/vllm/issues/12183) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to use beamsearch with llm.chat

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the code: ```python beam_params = BeamSearchParams(beam_width=n, max_tokens=4096) conversation = message_formator(prompt, texts_imgs) #__LLM.llm_engine.engine_args.limit_mm_per_prompt = {"image": im_count} outputs = __LLM.chat( messages = conversation, sampling_params=sampling_params, chat_template=CHAT_TEMPLATE, ) ``` Got the error: ```text rank0]: Traceback (most recent call last): [rank0]: File "/home/xxxxx/miniconda3/envs/xxxxx/lib/python3.10/runpy.py", line 196, in _run_module_as_main [rank0]: return _run_code(code, main_globals, None, [rank0]: File "/home/xxxxx/miniconda3/envs/xxxxx/lib/python3.10/runpy.py", line 86, in _run_code [rank0]: exec(code, run_globals) [rank0]: File "/home/xxxxx/.vscode-server/extensions/ms-python.debugpy-2024.14.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 71, in [rank0]: cli.main() [rank0]: File "/home/xxxxx/.vscode-server/extensions/ms-python.debugpy-2024.14.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 501, in main [rank0]: run() [rank0]:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: exec(code, run_globals) [rank0]: File "/home/xxxxx/xxxxx/refactored_version/vendors/deepseek__.py", line 124, in [rank0]: res = deepseek_vl2("help me", ["Tell what is the content in the images", img1, img2], n=3, temper...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: beamsearch with llm.chat bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the code: ```python beam_params = BeamSearchParams(beam_width=n, max_tokens=4096) conversa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Fail to use beamsearch with llm.chat bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the code: ```python beam_params = BeamSearchParams(beam_width=n, max_to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Fail to use beamsearch with llm.chat bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I run the code: ```python beam_params = BeamSearchParams(beam_width=n, max_to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
