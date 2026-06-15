# vllm-project/vllm#27228: [Installation]: Compatibility with PyTorch 2.9.0?

| 字段 | 值 |
| --- | --- |
| Issue | [#27228](https://github.com/vllm-project/vllm/issues/27228) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Compatibility with PyTorch 2.9.0?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm Is there a version of vllm that is compatible with the latest PyTorch release 2.9.0? ``` pip install vllm==0.11.0 pip install torch==2.9.0 ``` ``` $ vllm bench latency --input-len 256 --output-len 256 --model Qwen3/Qwen3-8B --batch-size 1 terminate called after throwing an instance of 'std::bad_alloc' what(): std::bad_alloc Aborted (core dumped) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Compatibility with PyTorch 2.9.0? installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm Is there a version of vllm that is compatibl
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ==2.9.0 ``` ``` $ vllm bench latency --input-len 256 --output-len 256 --model Qwen3/Qwen3-8B --batch-size 1 terminate called after throwing an instance of 'std::bad_alloc' what(): std::bad_alloc Aborted (core dumped) ``...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nstalling vllm Is there a version of vllm that is compatible with the latest PyTorch release 2.9.0? ``` pip install vllm==0.11.0 pip install torch==2.9.0 ``` ``` $ vllm bench latency --input-len 256 --output-len 256 --m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
