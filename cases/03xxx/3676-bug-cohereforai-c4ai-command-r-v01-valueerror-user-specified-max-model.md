# vllm-project/vllm#3676: [Bug]: CohereForAI/c4ai-command-r-v01 : ValueError: User-specified max_model_len (131072) is greater than the derived max_model_len (None=8192 in model's config.json). This may lead to incorrect model outputs or CUDA errors. Make sure the value is correct and within the model >

| 字段 | 值 |
| --- | --- |
| Issue | [#3676](https://github.com/vllm-project/vllm/issues/3676) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CohereForAI/c4ai-command-r-v01 : ValueError: User-specified max_model_len (131072) is greater than the derived max_model_len (None=8192 in model's config.json). This may lead to incorrect model outputs or CUDA errors. Make sure the value is correct and within the model >

### Issue 正文摘录

### Your current environment Head of main after various cohere updates/fixes. Issues: * Default is 8192 if don't do anything, but model card says 128k context: https://huggingface.co/CohereForAI/c4ai-command-r-v01 * Trying to change --max-model-len to 131072 fails with this error. ``` sudo apt update sudo apt install libnccl2 libnccl-dev wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run sudo sh cuda_12.1.0_530.30.02_linux.run sudo chmod -R a+rwx /usr/local/ export CUDA_HOME=/usr/local/cuda-12.1 export PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cu121" conda create -n vllm_cuda12.1 -y conda activate vllm_cuda12.1 conda install python=3.10 -y pip install git+https://github.com/vllm-project/vllm.git pip install hf_transfer pip install tiktoken accelerate flash_attn export HF_HUB_ENABLE_HF_TRANSFER=1 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/lib64:$HOME/extras/CUPTI/lib64 export PATH=$PATH:$CUDA_HOME/bin export CUDA_VISIBLE_DEVICES="0,1" python -m vllm.entrypoints.openai.api_server --port=5005 --host=0.0.0.0 --model CohereForAI/c4ai-command-r-v01 --seed 1234 --tensor-parallel-size=2 --max-num-batched-tokens=13...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CohereForAI/c4ai-command-r-v01 : ValueError: User-specified max_model_len (131072) is greater than the derived max_model_len (None=8192 in model's config.json). This may lead to incorrect model outputs or CUDA er...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: CohereForAI/c4ai-command-r-v01 : ValueError: User-specified max_model_len (131072) is greater than the derived max_model_len (None=8192 in model's config.json). This may lead to incorrect model outputs or CUDA er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 192 in model's config.json). This may lead to incorrect model outputs or CUDA errors. Make sure the value is correct and within the model > bug ### Your current environment Head of main after various cohere updates/fixe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ache;ci_build;distributed_parallel;frontend_api;model_support cuda crash;mismatch env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: host='0.0.0.0', port=5005, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, served_model_name=Non> Traceback (most recent call last):...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
