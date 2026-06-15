# vllm-project/vllm#19392: [Bug]: Error building vllm-cpu-dev image: torch==2.7.0+cu128 not found

| 字段 | 值 |
| --- | --- |
| Issue | [#19392](https://github.com/vllm-project/vllm/issues/19392) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error building vllm-cpu-dev image: torch==2.7.0+cu128 not found

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When building the vllm-cpu-dev image using the command: ```bash docker build -f docker/Dockerfile.cpu --target vllm-dev -t vllm-cpu-dev . ``` the build fails with the following error: ```text 0.193 Using Python 3.12.11 environment at: /opt/venv 9.622 × No solution found when resolving dependencies: 9.622 ╰─▶ Because there is no version of torch==2.7.0+cu128 and you require 9.622 torch==2.7.0+cu128, we can conclude that your requirements are 9.622 unsatisfiable. ``` The error occurs during the uv pip install -r requirements/dev.txt step. ------ **Steps to Reproduce:** - Clone the vllm repository. - Run the command: `docker build -f docker/Dockerfile.cpu --target vllm-dev -t vllm-cpu-dev . ` **Proposed Fix:** Modify Dockerfile.cpu, uv compile test.in before uv pip install all the test dependency. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Error building vllm-cpu-dev image: torch==2.7.0+cu128 not found bug ### Your current environment ### 🐛 Describe the bug When building the vllm-cpu-dev image using the command: ```bash docker build -f docker/Docke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing the uv pip install -r requirements/dev.txt step. ------ **Steps to Reproduce:** - Clone the vllm repository. - Run the command: `docker build -f docker/Dockerfile.cpu --target vllm-dev -t vllm-cpu-dev . ` **Proposed...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vllm-cpu-dev . ` **Proposed Fix:** Modify Dockerfile.cpu, uv compile test.in before uv pip install all the test dependency. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
