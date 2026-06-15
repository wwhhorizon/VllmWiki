# vllm-project/vllm#24481: [Bug]: Value error, Model architectures ['KeyeVL1_5ForConditionalGeneration'] are not supported for now

| 字段 | 值 |
| --- | --- |
| Issue | [#24481](https://github.com/vllm-project/vllm/issues/24481) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Value error, Model architectures ['KeyeVL1_5ForConditionalGeneration'] are not supported for now

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash export CUDA_VISIBLE_DEVICES=0 MODE_PATH=Kwai-Keye/Keye-VL-1.5-8B vllm serve $MODE_PATH\ --port 9010 \ --dtype bfloat16 \ --max-model-len 32768 \ --tensor-parallel-size 1\ --gpu-memory-utilization 0.9\ --served-model-name keye_vl \ --enable-prefix-caching \ --limit-mm-per-prompt '{"image": 4}'\ --trust_remote_code \ --disable-log-stats ``` when I run script，I get a error: Value error, Model architectures ['KeyeVL1_5ForConditionalGeneration'] are not supported for now ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;gemm;operator;triton build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e-VL-1.5-8B vllm serve $MODE_PATH\ --port 9010 \ --dtype bfloat16 \ --max-model-len 32768 \ --tensor-parallel-size 1\ --gpu-memory-utilization 0.9\ --served-model-name keye_vl \ --enable-prefix-caching \ --limit
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Value error, Model architectures ['KeyeVL1_5ForConditionalGeneration'] are not supported for now bug ### Your current environment ### 🐛 Describe the bug ```bash export CUDA_VISIBLE_DEVICES=0 MODE_PATH=Kwai-Keye/K...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d;distributed_parallel;hardware_porting;model_support cuda;gemm;operator;triton build_error dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Value error, Model architectures ['KeyeVL1_5ForConditionalGeneration'] are not supported for now bug ### Your current environment ### 🐛 Describe the bug ```bash export CUDA_VISIBLE_DEVICES=0 MODE_PATH=Kwai-Keye/K...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
