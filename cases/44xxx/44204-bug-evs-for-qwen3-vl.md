# vllm-project/vllm#44204: [Bug]: EVS for qwen3-vl

| 字段 | 值 |
| --- | --- |
| Issue | [#44204](https://github.com/vllm-project/vllm/issues/44204) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: EVS for qwen3-vl

### Issue 正文摘录

### Your current environment vllm 0.20.2, commit hash bc150f502 ### 🐛 Describe the bug ### Description vllm 0.20.2 crashes when working with EVS. ### How to trigger Just launch a qwen3-vl model with EVS on (--video_pruning_rate at any value in (0,1)), and send a request with video inputs. ```bash vllm serve /models/Qwen3-VL-8B-Instruct \ --port 8000 \ --served-model-name qwenvl \ --gpu-memory-utilization 0.80 \ --max-model-len 10000 \ --video_pruning_rate 0.5 \ ``` ### Error & relevant traces (EngineCore pid=1872) File "/home/g/vllm-workspace/libs/vllm/vllm/model_executor/models/qwen3_vl.py", line 2276, in _create_final_video_embeddings (EngineCore pid=1872) text_embeddings = self.get_language_model().embed_input_ids(repl_token_ids) (EngineCore pid=1872) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ... (EngineCore pid=1872) File "/home/g/vllm-workspace/libs/vllm/vllm/model_executor/layers/vocab_parallel_embedding.py", line 78, in embedding (EngineCore pid=1872) return F.embedding(input_, layer.weight) (EngineCore pid=1872) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=1872) File "/home/g/vllm-workspace/.venv/lib/python3.12/site-packages/torch/nn/functional.py", li...

## 现有链接修复摘要

#34246 [Core] Simplify multimodal masking

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: EVS for qwen3-vl bug ### Your current environment vllm 0.20.2, commit hash bc150f502 ### 🐛 Describe the bug ### Description vllm 0.20.2 crashes when working with EVS. ### How to trigger Just launch a qwen3-vl mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he same device, but got index is on cpu, different from other tensors on cuda:0 (when checking argument in method wrapper_CUDA__index_select) ### What caused the bug PR #34246 introduces a change to `_create_final_video...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns. performance frontend_api;model_support;multimodal_vlm cuda crash env_dependency #34246 [Core] Simplify multimodal masking Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ineCore pid=1872) return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse) (EngineCore pid=1872) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=1872) Runtim...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: del with EVS on (--video_pruning_rate at any value in (0,1)), and send a request with video inputs. ```bash vllm serve /models/Qwen3-VL-8B-Instruct \ --port 8000 \ --served-model-name qwenvl \ --gpu-memory-utilization 0...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34246](https://github.com/vllm-project/vllm/pull/34246) | mentioned | 0.45 | [Core] Simplify multimodal masking | ading to the crash. ### fix reverting this part of the change in pr #34246 will fix the bug. ### before submitting a new issue... - [x] make sure you already searched for relevant… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
