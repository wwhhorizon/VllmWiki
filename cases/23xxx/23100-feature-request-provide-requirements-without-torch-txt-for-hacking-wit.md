# vllm-project/vllm#23100: [feature request]: Provide `requirements_without_torch.txt` (for hacking with existing PyTorch)

| 字段 | 值 |
| --- | --- |
| Issue | [#23100](https://github.com/vllm-project/vllm/issues/23100) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [feature request]: Provide `requirements_without_torch.txt` (for hacking with existing PyTorch)

### Issue 正文摘录

Please add to docs an advice of how to install vllm with all its dependencies, but without downgrading already-installed pytorch version E.g. currently pip install-ing vllm leads to auto-downgrade of torch 2.8.0 to 2.7.1 which is not desirable if newer torch is already installed on the machine and the user is doing some experimentation. This should also make a much smaller-sized wheel and should not entail downloading of CUDA/nvidia dependency pacakages I also wonder if torch dependency could be replaced from `==` to `>=`. Given that both pytorch and vllm are evolving rapidly, probably this would simplify the life more than introduce incompat ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: king with existing PyTorch) usage Please add to docs an advice of how to install vllm with all its dependencies, but without downgrading already-installed pytorch version E.g. currently pip install-ing vllm leads to aut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and the user is doing some experimentation. This should also make a much smaller-sized wheel and should not entail downloading of CUDA/nvidia dependency pacakages I also wonder if torch dependency could be replaced from...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [feature request]: Provide `requirements_without_torch.txt` (for hacking with existing PyTorch) usage Please add to docs an advice of how to install vllm with all its dependencies, but without downgrading already-instal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api cuda env_dependency Please add to docs an advice of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
