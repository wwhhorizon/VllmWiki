# vllm-project/vllm#15991: [Bug]: amd gpu Multiple graphics cards cannot function properly

| 字段 | 值 |
| --- | --- |
| Issue | [#15991](https://github.com/vllm-project/vllm/issues/15991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: amd gpu Multiple graphics cards cannot function properly

### Issue 正文摘录

### Your current environment rocm 6.3.3 python3.12 Ubuntu 24.04 LTS AMD W6800 python3.12 -m venv vllm source bin/activate pip install --upgrade pip pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3 pip install /opt/rocm/share/amd_smi pip install --upgrade numba scipy huggingface-hub[cli] git clone https://github.com/vllm-project/vllm.git && cd vllm/requirements/ pip install -r rocm-build.txt #此文件需要修改 ################################### # Common dependencies -r common.txt #--extra-index-url https://download.pytorch.org/whl/rocm6.2.4 注释掉 #torch==2.6.0 注释掉 #torchvision==0.21.0 注释掉 #torchaudio==2.6.0 注释掉 cmake>=3.26, =61 setuptools-scm>=8 wheel jinja2>=3.1.6 #amdsmi==6.2.4 注释掉 ############################## pip install -r rocm.txt cd ../ export PYTORCH_ROCM_ARCH="gfx1030" python3 setup.py develop 0.8.3.dev221+g37bfee92.d20250403 1、python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --dtype=half --enable-reasoning --reasoning-parser deepseek_r1 Single graphics card running normally 2、python3 -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --dtype=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 24.04 LTS AMD W6800 python3.12 -m venv vllm source bin/activate pip install --upgrade pip pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3 pip install /opt/roc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: .3 pip install /opt/rocm/share/amd_smi pip install --upgrade numba scipy huggingface-hub[cli] git clone https://github.com/vllm-project/vllm.git && cd vllm/requirements/ pip install -r rocm-build.txt #此文件需要修改 ##########...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: amd gpu Multiple graphics cards cannot function properly bug;stale ### Your current environment rocm 6.3.3 python3.12 Ubuntu 24.04 LTS AMD W6800 python3.12 -m venv vllm source bin/activate pip install --upgrade p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: enai.api_server --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --dtype=half --enable-reasoning --reasoning-parser deepseek_r1 Single graphics card running normally 2、python3 -m vllm.entrypoints.openai.api_server --mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: s cards cannot function properly bug;stale ### Your current environment rocm 6.3.3 python3.12 Ubuntu 24.04 LTS AMD W6800 python3.12 -m venv vllm source bin/activate pip install --upgrade pip pip3 install --pre torch tor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
