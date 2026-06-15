# vllm-project/vllm#28903: [Bug]: vllm inference on qwen3-vl when use_upstream_fa is False

| 字段 | 值 |
| --- | --- |
| Issue | [#28903](https://github.com/vllm-project/vllm/issues/28903) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm inference on qwen3-vl when use_upstream_fa is False

### Issue 正文摘录

### Your current environment pip show torch vllm flash-attn Name: torch Version: 2.8.0 --- Name: vllm Version: 0.11.0 Name: flash_attn Version: 2.8.3 ### 🐛 Describe the bug unit-test code as the follows, when simple qwen3-0.6B can run; but qwen3-vl-4b not run ```python #coding=utf-8 """ 写单元测试来验证FA和VLLM的可用性和兼容性 """ import torch from flash_attn import flash_attn_func import unittest import vllm # from vllm.attention.backends import get_attn_backend class TestFA_VLLM(unittest.TestCase): def testFA(self,): # 检查CUDA是否可用及设备 print(f"CUDA available: {torch.cuda.is_available()}") print(f"Current device: {torch.cuda.current_device()}") print(f"Device name: {torch.cuda.get_device_name()}") # 尝试创建一个简单的张量并移动到GPU try: q = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda') k = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda') v = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda') output = flash_attn_func(q, k, v) print("FlashAttention test passed!") except Exception as e: print(f"FlashAttention test failed: {e}") def oriTestVLLM(self,): # 打印当前使用的attention后端 print("Available CUDA devices:", torch.cuda.device_count()) print("Current device:", torch.cuda.current_de...

## 现有链接修复摘要

#29889 [Bugfix] respect user-defined flash attention version in ViT attentions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ## Your current environment pip show torch vllm flash-attn Name: torch Version: 2.8.0 --- Name: vllm Version: 0.11.0 Name: flash_attn Version: 2.8.3 ### 🐛 Describe the bug unit-test code as the follows, when simple qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: class TestFA_VLLM(unittest.TestCase): def testFA(self,): # 检查CUDA是否可用及设备 print(f"CUDA available: {torch.cuda.is_available()}") print(f"Current device: {torch.cuda.current_device()}") print(f"Device name: {torch.cuda.get...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: import flash_attn_func import unittest import vllm # from vllm.attention.backends import get_attn_backend class TestFA_VLLM(unittest.TestCase): def testFA(self,): # 检查CUDA是否可用及设备 print(f"CUDA available: {torch.cuda.is_a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 试创建一个简单的张量并移动到GPU try: q = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda') k = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda') v = torch.randn(1, 1, 16, 64, dtype=torch.float16, device='cuda'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm inference on qwen3-vl when use_upstream_fa is False bug ### Your current environment pip show torch vllm flash-attn Name: torch Version: 2.8.0 --- Name: vllm Version: 0.11.0 Name: flash_attn Version: 2.8.3 #...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29889](https://github.com/vllm-project/vllm/pull/29889) | closes_keyword | 0.95 | [Bugfix] respect user-defined flash attention version in ViT attentions | fix #27103, #25143, #17392, #28903 in better way. ## Test Plan Run `Qwen/Qwen3-VL-32B-Instruct` successfully with the default FA backend on H100. ```bash vllm serve Qwen/Qwen3-V |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
