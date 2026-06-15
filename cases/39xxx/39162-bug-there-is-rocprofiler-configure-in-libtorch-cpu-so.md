# vllm-project/vllm#39162: [Bug]: There is "rocprofiler_configure" in libtorch_cpu.so

| 字段 | 值 |
| --- | --- |
| Issue | [#39162](https://github.com/vllm-project/vllm/issues/39162) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: There is "rocprofiler_configure" in libtorch_cpu.so

### Issue 正文摘录

### Your current environment Image: vllm/vllm-openai-rocm:nightly ROCM:7.2.1 torch: 2.10.0+git8514f05 vllm: 0.18.2rc1.dev25+gef53395e2.rocm721 I find that there is "rocprofiler_configure" in libtorch_cpu.so. But there isn`t in previous version(image:vllm/vllm-openai-rocm:latest) I can`t find "rocprofiler_configure" in the code of torch: 2.10.0. So why add the symbol? ### 🐛 Describe the bug as above ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: btorch_cpu.so bug ### Your current environment Image: vllm/vllm-openai-rocm:nightly ROCM:7.2.1 torch: 2.10.0+git8514f05 vllm: 0.18.2rc1.dev25+gef53395e2.rocm721 I find that there is "rocprofiler_configure" in libtorch_c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: There is "rocprofiler_configure" in libtorch_cpu.so bug ### Your current environment Image: vllm/vllm-openai-rocm:nightly ROCM:7.2.1 torch: 2.10.0+git8514f05 vllm: 0.18.2rc1.dev25+gef53395e2.rocm721 I find that t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: profiler_configure" in libtorch_cpu.so. But there isn`t in previous version(image:vllm/vllm-openai-rocm:latest) I can`t find "rocprofiler_configure" in the code of torch: 2.10.0. So why add the symbol? ### 🐛 Describe th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: There is "rocprofiler_configure" in libtorch_cpu.so bug ### Your current environment Image: vllm/vllm-openai-rocm:nightly ROCM:7.2.1 torch: 2.10.0+git8514f05 vllm: 0.18.2rc1.dev25+gef53395e2.rocm721 I find that t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
