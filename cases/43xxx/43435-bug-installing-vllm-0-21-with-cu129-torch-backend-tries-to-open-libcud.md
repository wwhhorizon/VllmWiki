# vllm-project/vllm#43435: [Bug]: installing vllm 0.21 with cu129 torch backend tries to open libcudart.so.13 which is specific to cu13

| 字段 | 值 |
| --- | --- |
| Issue | [#43435](https://github.com/vllm-project/vllm/issues/43435) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: installing vllm 0.21 with cu129 torch backend tries to open libcudart.so.13 which is specific to cu13

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to install vllm using the cu129 torch backend on python 3.14, with this command: ```bash uv pip install vllm==0.21 --torch-backend=cu129 ``` I get this error : ```bash × No solution found when resolving dependencies: ╰─▶ Because all versions of cuda-tile have no wheels with a matching Python ABI tag (e.g., `cp314`) and flashinfer-python==0.6.8.post1 depends on cuda-tile, we can conclude that flashinfer-python==0.6.8.post1 cannot be used. And because vllm==0.21.0 depends on flashinfer-python==0.6.8.post1 and you require vllm==0.21, we can conclude that your requirements are unsatisfiable. hint: Pre-releases are available for `cuda-tile` in the requested range (e.g., 1.0.0rc6), but pre-releases weren't enabled (try: `--prerelease=allow`) hint: You require CPython 3.14 (`cp314`), but we only found wheels for `cuda-tile` (v1.3.0) with the following Python ABI tags: `cp310`, `cp311`, `cp312`, `cp313` ``` When I allow prereleases (the setup is copied above) using this command ```bash uv pip install vllm==0.21 --torch-backend=cu129 --prerelease=allow ``` It installed correctly, but when I try to test it using this ```bash uv...

## 现有链接修复摘要

#43478 bugfix: add cu129 suffix to the cuda 12.9 wheel (#43435)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: installing vllm 0.21 with cu129 torch backend tries to open libcudart.so.13 which is specific to cu13 bug ### Your current environment ### 🐛 Describe the bug When trying to install vllm using the cu129 torch back...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: installing vllm 0.21 with cu129 torch backend tries to open libcudart.so.13 which is specific to cu13 bug ### Your current environment ### 🐛 Describe the bug When trying to install vllm using the cu129 torch back...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: installing vllm 0.21 with cu129 torch backend tries to open libcudart.so.13 which is specific to cu13 bug ### Your current environment ### 🐛 Describe the bug When trying to install vllm using the cu129 torch back...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3.14/site-packages/vllm/entrypoints/llm.py", line 21, in from vllm.config import ( ... ... ) File "/home/data/medical-nlp/atk7/test/.venv/lib/python3.14/site-packages/vllm/config/__init__.py", line 6, in from vllm.confi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error;crash;import_error env_dependency #43478 bugfix: add cu129 suffix to th...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43478](https://github.com/vllm-project/vllm/pull/43478) | closes_keyword | 0.95 | bugfix: add cu129 suffix to the cuda 12.9 wheel (#43435) | fix the #43435 bug which is currently breaking vLLM on cu129 setups the release pipeline already has separate wheel builds for cuda 12.9 and cuda 13. but the cuda 12.9 wheel nee |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
