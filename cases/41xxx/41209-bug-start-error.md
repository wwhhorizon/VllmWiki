# vllm-project/vllm#41209: [Bug]: start error

| 字段 | 值 |
| --- | --- |
| Issue | [#41209](https://github.com/vllm-project/vllm/issues/41209) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: start error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 启动 vLLM 服务器... Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 25, in from vllm.config import ModelConfig, VllmConfig File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/config/__init__.py", line 6, in from vllm.config.compilation import ( File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/config/compilation.py", line 22, in from vllm.platforms import current_platform File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/platforms/__init__.py", line 278, in __getattr__ _current_platform = resolve_obj_by_qualname(platform_cls_qualname)() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/utils/import_utils.py", line 109, in resolve_obj_by_qualname module = importlib.import_module(module_name) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lm/entrypoints/openai/api_server.py", line 25, in from vllm.config import ModelConfig, VllmConfig File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/config/__init__.py", line 6, in from vllm.config.compilatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/platforms/cuda.py", line 21, in import vllm._C # noqa ^^^^^^^^^^^^^^ ImportError: libcudart.so.13: cannot open shared object file: No such file or directory...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ages/vllm/entrypoints/openai/api_server.py", line 25, in from vllm.config import ModelConfig, VllmConfig File "/data/prod_vllm/.venv/lib/python3.12/site-packages/vllm/config/__init__.py", line 6, in from vllm.config.com...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;crash;import_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;crash;import_error;nan_inf env_dep...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
