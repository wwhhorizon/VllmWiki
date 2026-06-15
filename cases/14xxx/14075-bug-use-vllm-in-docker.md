# vllm-project/vllm#14075: [Bug]:use vllm in docker

| 字段 | 值 |
| --- | --- |
| Issue | [#14075](https://github.com/vllm-project/vllm/issues/14075) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | fp8;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:use vllm in docker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It work fine on conda envirentment ,but I build a docker image and run it, something was wrong. ```` vllm:0.7.2 model: qwen2.5 72b fp8, gpu: H100x2 nvlink ram: 256 gb docker base: pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]:use vllm in docker bug ### Your current environment ### 🐛 Describe the bug It work fine on conda envirentment ,but I build a docker image and run it, something was wrong. ```` vllm:0.7.2 model: qwen2.5 72b fp8, gp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ge and run it, something was wrong. ```` vllm:0.7.2 model: qwen2.5 72b fp8, gpu: H100x2 nvlink ram: 256 gb docker base: pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime development ci_build;distributed_parallel;model_suppo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it, something was wrong. ```` vllm:0.7.2 model: qwen2.5 72b fp8, gpu: H100x2 nvlink ram: 256 gb docker base: pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime development ci_build;distributed_parallel;model_support;quantiza...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I build a docker image and run it, something was wrong. ```` vllm:0.7.2 model: qwen2.5 72b fp8, gpu: H100x2 nvlink ram: 256 gb docker base: pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime development ci_build;distributed_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: parallel;model_support;quantization;scheduler_memory fp8;kernel;operator;triton build_error;crash dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
