# vllm-project/vllm#36530: [Bug]: pip install 0.17 fails with CXXABI_1.3.15 not found

| 字段 | 值 |
| --- | --- |
| Issue | [#36530](https://github.com/vllm-project/vllm/issues/36530) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pip install 0.17 fails with CXXABI_1.3.15 not found

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM 0.17.0 crashes when loading LLM module. ``` (vllm) [jlquinn@login5 synth]$ python -c "from vllm import LLM" INFO 03-09 18:42:41 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 03-09 18:42:41 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. Traceback (most recent call last): File " ", line 1, in File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/python3.12/site-packages/vllm/__init__.py", line 70, in __getattr__ module = import_module(module_name, __package__) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/python3.12/importlib/__init__.py", line 90, in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 48, in from vllm.entrypoints.pooling.io_processor_factories import init_pooling_io_processors File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: pip install 0.17 fails with CXXABI_1.3.15 not found bug ### Your current environment ### 🐛 Describe the bug VLLM 0.17.0 crashes when loading LLM module. ``` (vllm) [jlquinn@login5 synth]$ python -c "from vllm imp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: packages/vllm/v1/engine/input_processor.py", line 20, in from vllm.multimodal.encoder_budget import MultiModalBudget File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/python3.12/site-packages/vllm/multimodal/encode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: $ python -c "from vllm import LLM" INFO 03-09 18:42:41 [importing.py:44] Triton is installed but 0 active driver(s) found (expected 1). Disabling Triton to prevent runtime errors. INFO 03-09 18:42:41 [importing.py:68] T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in from vllm.entrypoints.openai.engine.serving import RendererChatRequest, RendererRequest File "/proj/dmfexp/jlquinn/sw/miniforge3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/openai/engine/serving.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
