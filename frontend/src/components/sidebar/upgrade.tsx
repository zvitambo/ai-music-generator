"use client";

import { authClient } from "~/lib/auth-client";
import { Button } from "../ui/button";
import { checkout } from "@polar-sh/better-auth";

export default function Upgrade() {
  const upgrade = async () => {
    await authClient.checkout({
      products: [
        "2b779a70-8fce-4098-aad3-2613d8aedcf5",
        "e087922f-9966-4b10-a0cf-f01d1ae86fff",
        "2ee96a7d-34c8-47a4-9035-0f3a901bc1e8",
      ],
    });
  };
  return (
    <Button
      variant="outline"
      size="sm"
      className="ml-2 cursor-pointer text-orange-400"
      onClick={upgrade}
    >
      Upgrade
    </Button>
  );
}
