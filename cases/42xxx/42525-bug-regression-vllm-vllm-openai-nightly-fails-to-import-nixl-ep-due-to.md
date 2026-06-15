# vllm-project/vllm#42525: [Bug]: Regression: vllm/vllm-openai:nightly fails to import nixl_ep due to missing libcudart.so.12

| 字段 | 值 |
| --- | --- |
| Issue | [#42525](https://github.com/vllm-project/vllm/issues/42525) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8 |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression: vllm/vllm-openai:nightly fails to import nixl_ep due to missing libcudart.so.12

### Issue 正文摘录

### Your current environment I believe this issue has regressed in the current `vllm/vllm-openai:nightly` image. I pulled and ran the Docker Hub `nightly` image from: `vllm/vllm-openai:nightly` and the server fails during model architecture inspection with the same `nixl_ep` / `libcudart.so.12` import error. ### 🐛 Describe the bug ## Image / vLLM version From the startup log: ```text version 0.20.2rc1.dev289+gdcacdf9a8 model RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Model ```text RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Relevant vLLM arguments ```text --model RedHatAI/gemma-4-31B-it-NVFP4 --served-model-name gemma4-31b --trust-remote-code --max-model-len 256000 --kv-cache-dtype fp8 --reasoning-parser gemma4 --tool-call-parser gemma4 --enable-auto-tool-choice --default-chat-template-kwargs '{"enable_thinking": true}' ``` ## Error The failure happens while inspecting `Gemma4ForConditionalGeneration`. The important part of the traceback is: ```text File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/prepare_finalize/nixl_ep.py", line 5, in import nixl_ep File "/usr/local/lib/python3.12/dist-packages/nixl_ep/__init__.py", line 23, in from . import nixl_ep_cpp as...

## 现有链接修复摘要

#42567 [CI] Add NIXL EP import canary

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Regression: vllm/vllm-openai:nightly fails to import nixl_ep due to missing libcudart.so.12 bug ### Your current environment I believe this issue has regressed in the current `vllm/vllm-openai:nightly` image. I p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: text version 0.20.2rc1.dev289+gdcacdf9a8 model RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Model ```text RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Relevant vLLM arguments ```text --model RedHatAI/gemma-4-31B-it-NVFP4 --served-model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: sion: vllm/vllm-openai:nightly fails to import nixl_ep due to missing libcudart.so.12 bug ### Your current environment I believe this issue has regressed in the current `vllm/vllm-openai:nightly` image. I pulled and ran...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ly` image from: `vllm/vllm-openai:nightly` and the server fails during model architecture inspection with the same `nixl_ep` / `libcudart.so.12` import error. ### 🐛 Describe the bug ## Image / vLLM version From the star...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: artup log: ```text version 0.20.2rc1.dev289+gdcacdf9a8 model RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Model ```text RedHatAI/gemma-4-31B-it-NVFP4 ``` ## Relevant vLLM arguments ```text --model RedHatAI/gemma-4-31B-it-NVFP4...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42567](https://github.com/vllm-project/vllm/pull/42567) | mentioned | 0.6 | [CI] Add NIXL EP import canary | ive accuracy sweep if the EP extension is not importable. Related to #42525 and #42542. ## Testing - `uv venv --python 3.12` - `.venv/bin/python -m py_compile tests/v1/kv_connecto… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
