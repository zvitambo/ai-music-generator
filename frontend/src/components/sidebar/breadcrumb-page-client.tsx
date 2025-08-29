"use client"

import { usePathname } from "next/navigation";
import { B } from "node_modules/better-auth/dist/shared/better-auth.DPa2nz5L";
import { BreadcrumbPage } from "../ui/breadcrumb";

export default function BreadcrumbPageClient() {

    const path = usePathname();
  return (
    <BreadcrumbPage>
      {path === "/" && "Home"}
      {path === "/create" && "Create"}
    </BreadcrumbPage>
  );
}