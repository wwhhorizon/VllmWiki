# vllm-project/vllm#2289: Issue when run distributed inference with vLLM + Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#2289](https://github.com/vllm-project/vllm/issues/2289) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Issue when run distributed inference with vLLM + Ray

### Issue 正文摘录

Steps: 1. Setting up a K8s cluster with two nodes, and each node have a Nvidia 3090 GPU. 2. Install Ray cluster using kuberay with one head and one worker pod 3. Use the command below to load model with single GPU by setting --tensor-parallel-size=1, **it works fine** ``` python3.8 -m vllm.entrypoints.api_server --model qwen-7b-chat --tensor-parallel-size 1 --trust-remote-code ``` use nvidia-smi to check GPU usage: ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535.54.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA GeForce RTX 3090 On | 00000000:3B:00.0 Off | N/A | | 0% 36C P2 105W / 350W | 21232MiB / 24576MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ ``` 5. Try the distributed inference, install vLLM package on...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: p a K8s cluster with two nodes, and each node have a Nvidia 3090 GPU. 2. Install Ray cluster using kuberay with one head and one worker pod 3. Use the command below to load model with single GPU by setting --tensor-para...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wen-7b-chat --tensor-parallel-size 1 --trust-remote-code ``` use nvidia-smi to check GPU usage: ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uberay with one head and one worker pod 3. Use the command below to load model with single GPU by setting --tensor-parallel-size=1, **it works fine** ``` python3.8 -m vllm.entrypoints.api_server --model qwen-7b-chat --t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
