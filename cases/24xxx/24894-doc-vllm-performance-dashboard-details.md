# vllm-project/vllm#24894: [Doc]: vllm performance dashboard details

| 字段 | 值 |
| --- | --- |
| Issue | [#24894](https://github.com/vllm-project/vllm/issues/24894) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: vllm performance dashboard details

### Issue 正文摘录

### 📚 The doc issue I am trying to replicate on a H100 machine the vllm performance dashboard data seen here: https://hud.pytorch.org/benchmark/llms?repoName=vllm-project/vllm. Could someone possibly assist me in obtaining information such as the dataset being utilised,the amount of prompts, input and output token length etc that must be followed in order to obtain the comparable statistics displayed on the dashboard? @simon-mo @ProExpertProg @hmellor @xuechendi @yeqcharlotte your comments on this would be really appreciated. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s documentation;stale ### 📚 The doc issue I am trying to replicate on a H100 machine the vllm performance dashboard data seen here: https://hud.pytorch.org/benchmark/llms?repoName=vllm-project/vllm. Could someone possib...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e the vllm performance dashboard data seen here: https://hud.pytorch.org/benchmark/llms?repoName=vllm-project/vllm. Could someone possibly assist me in obtaining information such as the dataset being utilised,the amount...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lor @xuechendi @yeqcharlotte your comments on this would be really appreciated. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Name=vllm-project/vllm. Could someone possibly assist me in obtaining information such as the dataset being utilised,the amount of prompts, input and output token length etc that must be followed in order to obtain the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: tain the comparable statistics displayed on the dashboard? @simon-mo @ProExpertProg @hmellor @xuechendi @yeqcharlotte your comments on this would be really appreciated. ### Suggest a potential alternative/fix _No respon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
