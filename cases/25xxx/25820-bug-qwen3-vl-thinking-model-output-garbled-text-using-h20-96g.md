# vllm-project/vllm#25820: [Bug]: Qwen3-Vl Thinking model output garbled text(Using H20 96G)

| 字段 | 值 |
| --- | --- |
| Issue | [#25820](https://github.com/vllm-project/vllm/issues/25820) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;gemm;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Vl Thinking model output garbled text(Using H20 96G)

### Issue 正文摘录

### Your current environment Cuda Version: 12 ### 🐛 Describe the bug Reproduce: Install: ```bash # 2025.9.28 latest code about transformers and vllm pip install git+https://gh.llkk.cc/https://github.com/huggingface/transformers pip install accelerate pip install qwen-vl-utils==0.0.14 export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple/ uv pip install -U vllm --system --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly ``` start vllm ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /model/Qwen3-VL-235B-A22B-Thinking \ --served-model-name Qwen3-VL-235B-A22B-Thinking \ --tensor-parallel-size 8 \ --mm-encoder-tp-mode data \ --limit-mm-per-prompt.video 0 \ --mm-processor-cache-type shm \ --enable-expert-parallel \ --host 0.0.0.0 \ --port 22002 \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --quantization fp8 \ --distributed-executor-backend mp ``` test.py ```python import time from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://127.0.0.1:22002/v1", timeout=3600 ) messages = [ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": "https://ofasys-multimodal-wlcb-3-toshanghai.oss-accelerate.aliy...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: output garbled text(Using H20 96G) bug ### Your current environment Cuda Version: 12 ### 🐛 Describe the bug Reproduce: Install: ```bash # 2025.9.28 latest code about transformers and vllm pip install git+https://gh.llkk...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: m \ --enable-expert-parallel \ --host 0.0.0.0 \ --port 22002 \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --quantization fp8 \ --distributed-executor-backend mp ``` test.py ```python import time from openai impo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-Vl Thinking model output garbled text(Using H20 96G) bug ### Your current environment Cuda Version: 12 ### 🐛 Describe the bug Reproduce: Install: ```bash # 2025.9.28 latest code about transformers and vllm...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: mit-mm-per-prompt.video 0 \ --mm-processor-cache-type shm \ --enable-expert-parallel \ --host 0.0.0.0 \ --port 22002 \ --dtype bfloat16 \ --gpu-memory-utilization 0.95 \ --quantization fp8 \ --distributed-executor-backe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: odel output garbled text(Using H20 96G) bug ### Your current environment Cuda Version: 12 ### 🐛 Describe the bug Reproduce: Install: ```bash # 2025.9.28 latest code about transformers and vllm pip install git+https://gh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
