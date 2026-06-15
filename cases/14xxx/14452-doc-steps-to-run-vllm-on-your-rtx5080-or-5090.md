# vllm-project/vllm#14452: [Doc]: Steps to run vLLM on your RTX5080 or 5090!

| 字段 | 值 |
| --- | --- |
| Issue | [#14452](https://github.com/vllm-project/vllm/issues/14452) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 137; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Steps to run vLLM on your RTX5080 or 5090!

### Issue 正文摘录

### 📚 The doc issue Let's take a look at the steps required to run vLLM on your RTX5080/5090! 1. **Initial Setup:** To start with, we need a container that has CUDA 12.8 and PyTorch 2.6 so that we have nvcc that can compile for Blackwell. ``` docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \ -it nvcr.io/nvidia/pytorch:25.02-py3 /bin/bash ``` 2. **Clone vLLM Repository:** Let's clone top of tree vLLM. If you have an existing clone or working directory, ensure that you are at or above the commit [ed6ea06](https://github.com/vllm-project/vllm/commit/ed6ea06577ec06f0b3a9ac921b55ef254f19d923) in your clone. ``` git clone https://github.com/vllm-project/vllm.git && cd vllm ``` 3. **Build vLLM in the container:** Now, we start building vLLM. Please note here that we can't use precompiled vLLM because `vllm-project/vllm` has not moved to the required torch and CUDA versions yet. So, we leverage the torch and CUDA versions that come with the NGC containers. The following steps are your standard build from source instructions, with the caveat of running `use_existing_torch.py` ``` python use_existing_torch.py pip install -r requirements/build.txt pip install set...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ntainer that has CUDA 12.8 and PyTorch 2.6 so that we have nvcc that can compile for Blackwell. ``` docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \ -it nvcr.io/nvidia/pytorch:25.02-py3 /bi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Doc]: Steps to run vLLM on your RTX5080 or 5090! documentation;stale ### 📚 The doc issue Let's take a look at the steps required to run vLLM on your RTX5080/5090! 1. **Initial Setup:** To start with, we need a containe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 7.4`+ Congratulations, your RTX5080/90 is now ready to run vLLM! Note: Flash Attention 3 backend doesn't work with Blackwell yet, please use `VLLM_FLASH_ATTN_VERSION=2` if you run into any issues. Thanks @ywang96 for te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Steps to run vLLM on your RTX5080 or 5090! documentation;stale ### 📚 The doc issue Let's take a look at the steps required to run vLLM on your RTX5080/5090! 1. **Initial Setup:** To start with, we need a containe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: l permissions for making changes to vLLM source in the container. 4. **Test vLLM**: Once your build succeeds, run the following to check your installation. ``` python -c "import vllm; print(vllm.__version__)" ``` You sh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
