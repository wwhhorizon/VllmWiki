# vllm-project/vllm#13171: [Bug]: InternVL2.5 broken after migration to new multi-model input

| 字段 | 值 |
| --- | --- |
| Issue | [#13171](https://github.com/vllm-project/vllm/issues/13171) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | gemm;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: InternVL2.5 broken after migration to new multi-model input

### Issue 正文摘录

### Your current environment docker + RTX 4090 ### 🐛 Describe the bug When running ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-openai:v0.7.0 --model OpenGVLab/InternVL2_5-8B ``` A request like ``` curl http://localhost:8080/v1/chat/completions \ -X POST \ -H 'Content-Type: application/json' \ -d '{ "model": "OpenGVLab/InternVL2_5-8B", "messages": [ { "role": "system", "content": "You are a bot specializing in image captioning." }, { "role": "user", "content": [{"type": "text", "text": "What is in this image?"}, {"type": "image_url", "image_url": {"url": "https://preview.redd.it/f58v4g8mwh551.jpg?auto=webp&s=8d987c7cfceb1feadb2925dfeabf15d050347543"}}] } ], "stream": false, "max_tokens": 2000, "temperature": 0 }' ``` works. But after last update, which includes #12553 this now happens: ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-openai --model OpenGVLab/InternVL2_5-8B --limit-mm-per-prompt image=2 ``` ``` curl http://localhost:8080/v1/chat/completions \ -X POST \ -H 'Content-Type: application/json' \ -d '{ "model": "OpenGVLab/InternVL2_5-8B", "messages": [ { "role": "system", "content": "You are a bot specializing in image captioning." }, { "role": "...

## 现有链接修复摘要

#12553 [VLM] Merged multi-modal processor for InternVL-based models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ter migration to new multi-model input bug ### Your current environment docker + RTX 4090 ### 🐛 Describe the bug When running ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-openai:v0.7.0 --model OpenGVLab/I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: InternVL2.5 broken after migration to new multi-model input bug ### Your current environment docker + RTX 4090 ### 🐛 Describe the bug When running ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-opena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion to new multi-model input bug ### Your current environment docker + RTX 4090 ### 🐛 Describe the bug When running ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-openai:v0.7.0 --model OpenGVLab/InternVL2_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: feabf15d050347543"}}] } ], "stream": false, "max_tokens": 2000, "temperature": 0 }' ``` works. But after last update, which includes #12553 this now happens: ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-o...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: estions. development ci_build;frontend_api;model_support;sampling_logits gemm;sampling #12553 [VLM] Merged multi-modal processor for InternVL-based models Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12553](https://github.com/vllm-project/vllm/pull/12553) | mentioned | 0.45 | [VLM] Merged multi-modal processor for InternVL-based models | ture": 0 }' ``` works. but after last update, which includes #12553 this now happens: ``` docker run --gpus all -p 8080:8000 --ipc=host vllm/vllm-openai --model opengvlab/inter |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
