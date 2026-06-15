# vllm-project/vllm#9939: [Bug]: from vllm.platforms import current_platform infinite loop error with OpenVino Build. 

| 字段 | 值 |
| --- | --- |
| Issue | [#9939](https://github.com/vllm-project/vllm/issues/9939) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: from vllm.platforms import current_platform infinite loop error with OpenVino Build. 

### Issue 正文摘录

### Your current environment Unrelated ### Model Input Dumps Unrelated ### 🐛 Describe the bug In OpenVino Build, from vllm.platforms import current_platform for OpenVino will... * reference openvino.py in vllm.platforms.openvino.py as OpenVino is identified as current platform * openvino.py line 4 will reference from vllm.utils import print_warning_once * vllm.utils line 40 will reference from vllm.platforms import current_platform * Due to circular self-reference, will throw error This impacts any vllm functionality on the openvino build due to vllm requiring detection of the current_platform. Resolution: **removing print_warning_once dependency from openvino.py will fix, either by defining print function locally or removing logging altogether from openvino.py** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: from vllm.platforms import current_platform infinite loop error with OpenVino Build. bug ### Your current environment Unrelated ### Model Input Dumps Unrelated ### 🐛 Describe the bug In OpenVino Build, from vllm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: r with OpenVino Build. bug ### Your current environment Unrelated ### Model Input Dumps Unrelated ### 🐛 Describe the bug In OpenVino Build, from vllm.platforms import current_platform for OpenVino will... * reference op...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
