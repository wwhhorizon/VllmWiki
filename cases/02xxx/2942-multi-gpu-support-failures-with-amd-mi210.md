# vllm-project/vllm#2942: Multi-GPU Support Failures with AMD MI210

| 字段 | 值 |
| --- | --- |
| Issue | [#2942](https://github.com/vllm-project/vllm/issues/2942) |
| 状态 | closed |
| 标签 | rocm;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;kernel;quantization |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Multi-GPU Support Failures with AMD MI210

### Issue 正文摘录

Hello. Thank for providing vLLM as a great open-source tool for inference and model serving! I was able to build vLLM on a cluster I maintain, but it only appears to work on a single MI210 GPU. Can someone please help me with this issue? The details of my attempt are as follows... This is how I built vLLM on a node comprised of [2x] 64-core AMD EPYC CPUs and [4x] AMD MI210 GPUs with ROCm 5.7.1 installed: ``` ## STEP 0: Create new Python virtual environment and activate it python -m venv venv source venv/bin/activate ## STEP 1: Install ROCm-enabled PyTorch pip install --upgrade pip pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7 ## STEP 2: Build and install flash-attention package git clone --recursive https://github.com/ROCmSoftwarePlatform/flash-attention.git cd flash-attention export GPU_ARCHS="gfx90a" export PYTHON_SITE_PACKAGES=$(python -c 'import site; print(site.getsitepackages()[0])') pip install packaging pip install --upgrade setuptools wheel # Upgrading wheel was necessary to avoid build issues pip install . # This takes multiple hours for some reason, but not your problem : ) ## STEP 3: Install xformers pip install xformers=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: a great open-source tool for inference and model serving! I was able to build vLLM on a cluster I maintain, but it only appears to work on a single MI210 GPU. Can someone please help me with this issue? The details of m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: . Thank for providing vLLM as a great open-source tool for inference and model serving! I was able to build vLLM on a cluster I maintain, but it only appears to work on a single MI210 GPU. Can someone please help me wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Multi-GPU Support Failures with AMD MI210 rocm;stale Hello. Thank for providing vLLM as a great open-source tool for inference and model serving! I was able to build vLLM on a cluster I maintain, but it only appears to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantiza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
