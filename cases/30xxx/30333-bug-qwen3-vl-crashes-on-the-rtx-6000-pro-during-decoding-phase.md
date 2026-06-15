# vllm-project/vllm#30333: [Bug]: Qwen3-VL Crashes on the RTX 6000 Pro during decoding phase

| 字段 | 值 |
| --- | --- |
| Issue | [#30333](https://github.com/vllm-project/vllm/issues/30333) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL Crashes on the RTX 6000 Pro during decoding phase

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes due to flash-attention on the RTX 6000 PRO. When switching to FlashInfer, it says it's not supported for Qwen3-VL but the FlashInfer attention backend actually works Qwen3VL + sm_120 in SGLang. I spent sometime building vLLM for sm_120 but other issues pop-up. This issue happens with Qwen3-8B too, not just the VL version. I tried this as suggested in the doc mentioned in similar issues but it just hangs in `Capturing CUDA graphs (decode, FULL):` ``` sudo apt-get install cuda-compat-12-9 export LD_LIBRARY_PATH=/usr/local/cuda-12.9/compat:$LD_LIBRARY_PATH ``` Any tips to get this working? Thank you very much in advance 🙏 ``` python3 -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-VL-8B-Instruct-FP8 \ --max-model-len 16384 \ --max-num-batched-tokens 8192 \ --mm_encoder_tp_mode "data"\ --limit-mm-per-prompt.video 0 \ --async-scheduling \ --skip-mm-profiling \ --no-enable-log-requests \ --host 0.0.0.0 \ --port 8000 ``` Error: ``` (EngineCore_DP0 pid=6978) File "/usr/local/lib/python3.12/dist-packages/vllm/attention/layer.py", line 869, in unified_attention_with_output (EngineCore_DP0 pid=6978) self.impl.for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ion backend actually works Qwen3VL + sm_120 in SGLang. I spent sometime building vLLM for sm_120 but other issues pop-up. This issue happens with Qwen3-8B too, not just the VL version. I tried this as suggested in the d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Qwen3-VL Crashes on the RTX 6000 Pro during decoding phase bug ### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes due to flash-attention on the RTX 6000 PRO. When switching to FlashInfer, it say...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm.entrypoints.openai.api_server \ --model Qwen/Qwen3-VL-8B-Instruct-FP8 \ --max-model-len 16384 \ --max-num-batched-tokens 8192 \ --mm_encoder_tp_mode "data"\ --limit-mm-per-prompt.video 0 \ --async-scheduling \ --skip...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL Crashes on the RTX 6000 Pro during decoding phase bug ### Your current environment ### 🐛 Describe the bug Qwen3-VL crashes due to flash-attention on the RTX 6000 PRO. When switching to FlashInfer, it say...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mentioned in similar issues but it just hangs in `Capturing CUDA graphs (decode, FULL):` ``` sudo apt-get install cuda-compat-12-9 export LD_LIBRARY_PATH=/usr/local/cuda-12.9/compat:$LD_LIBRARY_PATH ``` Any tips to get...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
