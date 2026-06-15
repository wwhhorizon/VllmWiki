# vllm-project/vllm#24865: [Bug]: v0.10.2 Qwen 3 Next 80b FP8 Slow first request and potential format mismatch: seq_len (4) < num_heads (8)

| 字段 | 值 |
| --- | --- |
| Issue | [#24865](https://github.com/vllm-project/vllm/issues/24865) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | shape_align |
| Operator 关键词 | activation;fp8;operator;quantization |
| 症状 | mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.10.2 Qwen 3 Next 80b FP8 Slow first request and potential format mismatch: seq_len (4) < num_heads (8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using Qwen 3 Next 80b quantized to FP8 dynamic format using llm-compressor (recipe below) I have a very slow first request (15-20s TTFT) on 2xH100 SXM : I see the log entry for the incoming request : "POST /v1/chat/completions HTTP/1.1" 200 OK but it doesn't seem to run until 15 to 20s I also have multiple warnings of this type : (Worker_TP0 pid=124) /usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:929: UserWarning: Input tensor shape suggests potential format mismatch: seq_len (4) < num_heads (8). This may indicate the inputs were passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. (Worker_TP0 pid=124) return fn(*args, **kwargs) (Worker_TP1 pid=125) /usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:929: UserWarning: Input tensor shape suggests potential format mismatch: seq_len (4) < num_heads (8). This may indicate the inputs were passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Qwen 3 Next 80b quantized to FP8 dynamic format using llm-compressor (recipe below) I have a very slow first request (15-20s TTFT) on 2xH100 SXM : I see the log entry for the incoming request : "POST /v1/chat/completion...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: v0.10.2 Qwen 3 Next 80b FP8 Slow first request and potential format mismatch: seq_len (4) < num_heads (8) bug ### Your current environment ### 🐛 Describe the bug When using Qwen 3 Next 80b quantized to FP8 dynami...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: v0.10.2 Qwen 3 Next 80b FP8 Slow first request and potential format mismatch: seq_len (4) < num_heads (8) bug ### Your current environment ### 🐛 Describe the bug When using Qwen 3 Next 80b quantized to FP8 dynami...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: v0.10.2 Qwen 3 Next 80b FP8 Slow first request and potential format mismatch: seq_len (4) < num_heads (8) bug ### Your current environment ### 🐛 Describe the bug When using Qwen 3 Next 80b quantized to FP8 dynamic fo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: eme="FP8_DYNAMIC", ignore=["lm_head", "re:.*mlp.gate$", "re:.*mlp.shared_expert_gate$", 're:.*router$', 're:mtp.*', 're:.*input_layernorm$', 're:.*post_attention_layernorm$', 're:.*mlp[.]gate$', 're:.*shared_expert_gate...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
