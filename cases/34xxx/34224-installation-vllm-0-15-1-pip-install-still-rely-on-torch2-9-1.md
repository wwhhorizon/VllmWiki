# vllm-project/vllm#34224: [Installation]: vllm 0.15.1 pip install still rely on torch2.9.1

| 字段 | 值 |
| --- | --- |
| Issue | [#34224](https://github.com/vllm-project/vllm/issues/34224) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm 0.15.1 pip install still rely on torch2.9.1

### Issue 正文摘录

### Your current environment ```text torch 2.9.1 torchaudio 2.9.1 torchvision 0.24.1 tqdm 4.67.3 transformers 4.57.6 triton 3.5.1 typer 0.21.1 typing_extensions 4.15.0 typing-inspection 0.4.2 urllib3 2.6.3 uvicorn 0.40.0 uvloop 0.22.1 vllm 0.15.1 ``` ### How you are installing vllm ```sh python -m pip install vllm==0.15.1 ``` when install vllm==0.15.1, it will ``` Attempting uninstall: torch Found existing installation: torch 2.10.0+cu130 Uninstalling torch-2.10.0+cu130: Successfully uninstalled torch-2.10.0+cu130 Attempting uninstall: torchvision Found existing installation: torchvision 0.25.0+cu130 Uninstalling torchvision-0.25.0+cu130: Successfully uninstalled torchvision-0.25.0+cu130 Attempting uninstall: torchaudio Found existing installation: torchaudio 2.10.0+cu130 Uninstalling torchaudio-2.10.0+cu130: Successfully uninstalled torchaudio-2.10.0+cu130 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 4.67.3 transformers 4.57.6 triton 3.5.1 typer 0.21.1 typing_extensions 4.15.0 typing-inspection 0.4.2 urllib3 2.6.3 uvicorn
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: vllm 0.15.1 pip install still rely on torch2.9.1 installation ### Your current environment ```text torch 2.9.1 torchaudio 2.9.1 torchvision
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
