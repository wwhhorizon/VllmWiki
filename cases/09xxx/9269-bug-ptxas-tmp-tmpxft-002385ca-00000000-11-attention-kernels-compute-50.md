# vllm-project/vllm#9269: [Bug]:       ptxas /tmp/tmpxft_002385ca_00000000-11_attention_kernels.compute_50.ptx, line 4986061; error   : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

| 字段 | 值 |
| --- | --- |
| Issue | [#9269](https://github.com/vllm-project/vllm/issues/9269) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:       ptxas /tmp/tmpxft_002385ca_00000000-11_attention_kernels.compute_50.ptx, line 4986061; error   : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

### Issue 正文摘录

### Your current environment ![Uploading image.png…]() ![Uploading image.png…]() ### Model Input Dumps _No response_ ### 🐛 Describe the bug pip install git+https://github.com/vllm-project/vllm.git ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ptxas /tmp/tmpxft_002385ca_00000000-11_attention_kernels.compute_50.ptx, line 4986061; error : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher bug;stale ### Your current enviro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g…]() ### Model Input Dumps _No response_ ### 🐛 Describe the bug pip install git+https://github.com/vllm-project/vllm.git ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment ![Uploading image.png…]() ![Uploading image.png…]() ### Model Input Dumps _No response_ ### 🐛 Describe the bug pip install git+https://github.com/vllm-project/vllm.git ### Before submitting a new issue... -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ithemetic and compare instructions' requires .target sm_53 or higher bug;stale ### Your current environment ![Uploading image.png…]() ![Uploading image.png…]() ### Model Input Dumps _No response_ ### 🐛 Describe the bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
