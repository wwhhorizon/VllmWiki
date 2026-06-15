# vllm-project/vllm#21745: [Bug]: vllm ignores existing pytorch installation

| 字段 | 值 |
| --- | --- |
| Issue | [#21745](https://github.com/vllm-project/vllm/issues/21745) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm ignores existing pytorch installation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to build vllm with an existing nightly pytorch / custom triton build via: ``` pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128 #2.9 git clone https://github.com/vllm-project/vllm.git; cd vllm; python use_existing_torch.py; pip install -r requirements/build.txt; pip install --no-build-isolation -e .; #-> will uninstall the nightly build and use torch=2.7.1 ``` but it keeps ignoring the existing pytorch/triton setup and re-installs torch==2.7.1/triton==3.3.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm ignores existing pytorch installation bug ### Your current environment ### 🐛 Describe the bug I am trying to build vllm with an existing nightly pytorch / custom triton build via: ``` pip install --pre torch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 3.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bug I am trying to build vllm with an existing nightly pytorch / custom triton build via: ``` pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128 #2.9 git clone http...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting cuda;triton build_error en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
