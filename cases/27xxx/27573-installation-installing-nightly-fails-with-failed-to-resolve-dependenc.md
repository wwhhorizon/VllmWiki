# vllm-project/vllm#27573: [Installation]: Installing nightly fails with: Failed to resolve dependencies for `vllm`

| 字段 | 值 |
| --- | --- |
| Issue | [#27573](https://github.com/vllm-project/vllm/issues/27573) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | kernel;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installing nightly fails with: Failed to resolve dependencies for `vllm`

### Issue 正文摘录

### Your current environment No env yet ### How you are installing vllm Steps to reproduce: ```sh uv venv --python 3.13 --seed source .venv/bin/activate uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly ``` Installation fails with: ``` (vllm.313) drros@tesla:~/vllm.313$ uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly × Failed to resolve dependencies for `vllm` (v0.11.1rc4.dev30+gf4e815407.cu129) ╰─▶ Package `triton-kernels` was included as a URL dependency. URL dependencies must be expressed as direct requirements or constraints. Consider adding `triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels` to your dependencies or constraints file. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Installing nightly fails with: Failed to resolve dependencies for `vllm` installation;stale ### Your current environment No env yet ### How you are installing vllm Steps to reproduce: ```sh uv venv --py
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 3.13 --seed source .venv/bin/activate uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly ``` Installation fails with: ``` (vllm.313) drros@tesla:~/vllm.313$ uv pip install -U vl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: rrent environment No env yet ### How you are installing vllm Steps to reproduce: ```sh uv venv --python 3.13 --seed source .venv/bin/activate uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ghtly fails with: Failed to resolve dependencies for `vllm` installation;stale ### Your current environment No env yet ### How you are installing vllm Steps to reproduce: ```sh uv venv --python 3.13 --seed source .venv/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
