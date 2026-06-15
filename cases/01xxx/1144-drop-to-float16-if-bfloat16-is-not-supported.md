# vllm-project/vllm#1144: Drop to float16 if bfloat16 is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#1144](https://github.com/vllm-project/vllm/issues/1144) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Drop to float16 if bfloat16 is not supported

### Issue 正文摘录

Instead of throwing an error if the GPU compute capability is not supported for `bfloat16`, vLLM should throw a warning but use `float16` instead In `transformers_utils/config.py`: ``` # Check if the GPU supports the dtype. if torch_dtype == torch.bfloat16: compute_capability = torch.cuda.get_device_capability() if compute_capability[0] < 8: gpu_name = torch.cuda.get_device_name() raise ValueError( "Bfloat16 is only supported on GPUs with compute capability " f"of at least 8.0. Your {gpu_name} GPU has compute capability " f"{compute_capability[0]}.{compute_capability[1]}.") ``` Could be something like: ``` # Check if the GPU supports the dtype. if torch_dtype == torch.bfloat16: compute_capability = torch.cuda.get_device_capability() if compute_capability[0] < 8: gpu_name = torch.cuda.get_device_name() log.warning( "Bfloat16 is only supported on GPUs with compute capability " f"of at least 8.0. Your {gpu_name} GPU has compute capability " f"{compute_capability[0]}.{compute_capability[1]}. Dropping to float16") torch_dtype = torch.float16 ```

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Drop to float16 if bfloat16 is not supported Instead of throwing an error if the GPU compute capability is not supported for `bfloat16`, vLLM should throw a warning but use `float16` instead In `transformers_utils/confi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: float16 is not supported Instead of throwing an error if the GPU compute capability is not supported for `bfloat16`, vLLM should throw a warning but use `float16` instead In `transformers_utils/config.py`: ``` # Check i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ) torch_dtype = torch.float16 ``` development cuda dtype;env_dependency #41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: should throw a warning but use `float16` instead In `transformers_utils/config.py`: ``` # Check if the GPU supports the dtype. if torch_dtype == torch.bfloat16: compute_capability = torch.cuda.get_device_capability() if...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | href="https://redirect.github.com/prometheus/client_python/pull/1144">prometheus/client_python#1144</a></li> <li>Add Django exporter (<a href="https://redirect.github.com/promethe… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
